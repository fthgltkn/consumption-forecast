from sklearn.model_selection import TimeSeriesSplit
from seffaflik.elektrik.tuketim import gerceklesen as tuk_gerceklesen
from seffaflik.elektrik.uretim import gerceklesen as uret_gerceklesen
from sklearn.metrics import mean_absolute_error
from catboost import CatBoostRegressor
import plotly.graph_objects as go
import plotly.express as px
from tqdm import tqdm
import pandas as pd
import numpy as np

def select_period(period):
    periods={"1 gün":24,"2 gün":48,"3 gün":72,"1 hafta":168,"2 hafta":336}
    return periods[period]

def get_uretim_data(start_date, kaynak=None):
    df = uret_gerceklesen(start_date).iloc[:-1,:]
    df['Tarih'] = pd.to_datetime(df['Tarih']) + pd.to_timedelta(df['Saat'], unit='h')
    df.drop(columns='Saat', inplace=True)
    df.rename(columns={'Tarih': 'date'}, inplace=True)
    df = df[['date', kaynak]]
    return df

def get_consumption_data(start_date):
    df = tuk_gerceklesen(start_date).iloc[:-1,:]
    df['Tarih'] = pd.to_datetime(df['Tarih']) + pd.to_timedelta(df['Saat'], unit='h')
    df.drop(columns='Saat', inplace=True)
    df.rename(columns={'Tarih': 'date', 'Tüketim': 'consumption'}, inplace=True)
    return df


def rolling_features(df,fh, col_list):
    df_c=df.copy()
    rolling_windows=[fh,fh+3,fh+10,fh+15,fh+20,fh+25]
    lags=[fh,fh+5,fh+10,fh+15,fh+20,fh+30]
    for col in tqdm(col_list):
        for a in rolling_windows:
            df_c['rolling_mean_{}_{}'.format(col,a)]=df_c[col].rolling(a,min_periods=1).mean().shift(1)
            df_c['rolling_std_{}_{}'.format(col,a)]=df_c[col].rolling(a,min_periods=1).std().shift(1)
            df_c['rolling_min_{}_{}'.format(col,a)]=df_c[col].rolling(a,min_periods=1).min().shift(1)
            df_c['rolling_max_{}_{}'.format(col,a)]=df_c[col].rolling(a,min_periods=1).max().shift(1)
            df_c['rolling_var_{}_{}'.format(col,a)]=df_c[col].rolling(a,min_periods=1).var().shift(1)
    for col in tqdm(col_list):
        for l in lags:
            df_c['{}_lag_{}'.format(col,l)]=df_c[col].shift(l)
    return(df_c)

def date_features(df):
    df_c=df.copy()
    df_c['month']=df_c['date'].dt.month
    df_c['year']=df_c['date'].dt.year
    df_c['hour']=df_c['date'].dt.hour
    df_c['quarter']=df_c['date'].dt.quarter
    df_c['dayofweek']=df_c['date'].dt.dayofweek
    df_c['dayofyear']=df_c['date'].dt.dayofyear
    df_c['dayofmonth']=df_c['date'].dt.day
    df_c['weekofyear']=df_c['date'].dt.weekofyear
    return(df_c)

def forecast_func(df,fh, kaynak=None):
    # forecast datasının oluşturulması 
    fh_new=fh+1
    date=pd.date_range(start=df.date.tail(1).iloc[0],periods=fh_new,freq='H',name='date')
    date=pd.DataFrame(date)
    df_fe=pd.merge(df,date,how='outer')
    
    #feature engineering
    col_list=[kaynak]
    df_fe=rolling_features(df_fe,fh_new,col_list=col_list)
    df_fe=date_features(df_fe)
    df_fe=df_fe[fh_new+30:].reset_index(drop=True)

    # train-test split 
    split_date = df_fe[df_fe[kaynak].isnull()].iloc[0,0]

    historical_data = df_fe[df_fe['date'] < split_date]
    forecast_data = df_fe[df_fe['date'] >= split_date].drop(columns=[kaynak]).set_index('date')

    X = historical_data.drop(columns=[kaynak]).set_index('date')
    y = historical_data[['date', kaynak]].set_index('date')

    tscv = TimeSeriesSplit(n_splits=3, test_size=fh_new * 10)

    score_list = []
    fold = 1
    unseen_preds = []
    importance = []
    #cross validation step
    for train_index, test_index in tscv.split(X,y):
        X_train, X_val = X.iloc[train_index], X.iloc[test_index]
        y_train, y_val = y.iloc[train_index], y.iloc[test_index]
        print(X_train.shape,X_val.shape)

        catb = CatBoostRegressor(iterations=1000,eval_metric='MAE',allow_writing_files=False)
        catb.fit(X_train,y_train,eval_set=[(X_val,y_val)],early_stopping_rounds=150,verbose=50)

        unseen_preds.append(catb.predict(forecast_data))

        score = mean_absolute_error(y_val,catb.predict(X_val))
        print(f"MAE Fold-{fold} : {score}")
        score_list.append(score)
        importance.append(catb.get_feature_importance())
        fold+=1
    print("CV Mean Score:",np.mean(score_list))

    forecasted=pd.DataFrame(unseen_preds[2],columns=['forecasting']).set_index(forecast_data.index)

    fig1 = go.Figure()
    fig1.add_trace(go.Scatter(x=df_fe.date.iloc[-fh_new*5:],y=df_fe[kaynak].iloc[-fh_new*5:],name='Tarihsel Veri',mode='lines'))
    fig1.add_trace(go.Scatter(x=forecasted.index,y=forecasted["forecasting"],name='tahmin',mode='lines'))
    fig1.update_layout(legend=dict(orientation="h",yanchor="bottom",y=1.02,xanchor="right",x=1))
    f_importance=pd.concat([pd.Series(X.columns.to_list(),name="Feature"),pd.Series(np.mean(importance,axis=0),name="Importance")],axis=1).sort_values(by="Importance",ascending=True)
    fig2 = px.bar(f_importance.tail(10), x='Importance', y='Feature')
    forc_data = forecasted[["forecasting"]]
    return fig1, fig2, forc_data
