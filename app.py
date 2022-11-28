
from functions import *
import streamlit as st
import datetime
import warnings
import pandas as pd
import io
warnings.filterwarnings("ignore")

st.set_page_config(page_title="Tahmin Aracı")
tabs= ["Tahmin","Görselleştirme","Hakkında"]
page = st.sidebar.radio("Sekmeler",tabs)

if page == "Tahmin":
    st.markdown("<h1 style='text-align:center;'>Elektrik Tüketimi Tahmin Çalışması</h1>",unsafe_allow_html=True)
    st.write("""Bu sayfada tahmin uzunluğı seçilerek sonuçlar elde edilmektedir.""")
    fh_selection=st.selectbox("Tahmin uzunluğunu seçiniz",["1 gün","2 gün","3 gün","1 hafta","2 hafta"])
    button=st.button("Tahmin Et")

    if button==True:
        with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
            start_date="2016-01-01"
            df=get_consumption_data(start_date=str(start_date))
            fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection))
            st.markdown("<h3 style='text-align:center;'>Tahmin sonuçları</h3>",unsafe_allow_html=True)
            st.plotly_chart(fig1)
            st.markdown("<h3 style='text-align:center;'>Model için en önemli değişkenler</h3>",unsafe_allow_html=True)
            st.plotly_chart(fig2)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
            forc_data.to_excel(writer, sheet_name='Sheet1')
            writer.save()
            st.download_button(
                label="Download Excel forecasts",
                data=buffer,
                file_name="forecast.xlsx",
                mime="application/vnd.ms-excel"
            )

elif page == "Görselleştirme":
    st.markdown("<h1 style='text-align:center;'>Veri Görselleştirme Sekmesi</h1>",unsafe_allow_html=True)
    start_date=st.sidebar.date_input(label="Başlangıç Tarihi",value=datetime.date.today()-datetime.timedelta(days=10),max_value=datetime.date.today())
    df_vis = get_consumption_data(start_date=str(start_date))
    df_describe=pd.DataFrame(df_vis.describe())
    st.markdown("<h3 style='text-align:center;'>Tüketim-Tanımlayıcı İstatistikler</h3>",unsafe_allow_html=True)
    st.table(df_describe)

    fig3=go.Figure()
    fig3.add_trace(go.Scatter(x=df_vis.date,y=df_vis.consumption,mode='lines',name='Tüketim (MWh)'))
    fig3.update_layout(xaxis_title='Date',yaxis_title="Consumption")
    st.markdown("<h3 style='text-align:center;'>Saatlik Tüketim (MWh)</h3>",unsafe_allow_html=True)
    st.plotly_chart(fig3)

elif page == "Hakkında":
    st.header("Linkedin Profili")
    st.markdown("""**[Fatih Gültekin](https://www.linkedin.com/in/fatih-gultekin/)** """)