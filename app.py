import streamlit as st
import yfinance as yf
import datetime as date  

st.title('Stock Prediction App')
st.write("This app predicts the closing price of a stock for four months based on the data from the past 10 years.")
stocks = ('GME','GOOG', 'AAPL', 'MSFT')
stock = st.selectbox('Select dataset for prediction', stocks)
start = '2010-01-01'
end = date.datetime.now().strftime('%Y-%m-%d')

def read_data():
    data = yf.download(stock, start, end)
    return data
data = read_data()
st.subheader('Raw data')
st.write(data.tail())