
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
    st.markdown("<h1 style='text-align:center;'>Elektrik Tüketimi Ve Üretimi Tahmin Çalışması</h1>",unsafe_allow_html=True)
    st.write("""Bu sayfada tahmin uzunluğu seçilerek sonuçlar elde edilmektedir.""")
    sources = ['tüketim', 'Doğalgaz', 'Barajlı', 'Linyit', 'Akarsu','İthal Kömür', 'Rüzgar',
               'Güneş', 'Fuel Oil', 'Jeo Termal', 'Asfaltit Kömür', 'Taş Kömür', 'Biyokütle']

    source_select = st.selectbox('Hangi kaynağın tahmin edileceğini seçiniz', options=sources)
    fh_selection=st.selectbox("Tahmin uzunluğunu seçiniz",["1 gün","2 gün","3 gün","1 hafta","2 hafta"])
    button=st.button("Tahmin Et")
    if source_select == 'tüketim':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2016-01-01"
                df=get_consumption_data(start_date=str(start_date))
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection),kaynak='consumption')
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
    elif source_select == 'Doğalgaz':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Doğalgaz')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Doğalgaz')
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

    elif source_select == 'Barajlı':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Barajlı')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Barajlı')
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
    elif source_select == 'Linyit':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Linyit')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Linyit')
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
    elif source_select == 'Akarsu':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Akarsu')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Akarsu')
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
    elif source_select == 'İthal Kömür':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='İthal Kömür')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='İthal Kömür')
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
    elif source_select == 'Rüzgar':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Rüzgar')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Rüzgar')
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
    elif source_select == 'Güneş':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Güneş')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Güneş')
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

    elif source_select == 'Fuel Oil':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Fuel Oil')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Fuel Oil')
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

    elif source_select == 'Jeo Termal':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Jeo Termal')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Jeo Termal')
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

    elif source_select == 'Asfaltit Kömür':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Asfaltit Kömür')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Asfaltit Kömür')
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

    elif source_select == 'Taş Kömür':
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Taş Kömür')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Taş Kömür')
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

    else:
        if button==True:
            with st.spinner("Tahmin yapılıyor, lütfen bekleyiniz..."):
                start_date="2020-01-01"
                df=get_uretim_data(start_date=str(start_date), kaynak='Biyokütle')
                fig1,fig2,forc_data= forecast_func(df,select_period(fh_selection), kaynak='Biyokütle')
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