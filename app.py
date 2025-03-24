
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from src.prompt import *
import dotenv
import os,io
import streamlit as st
from dotenv import load_dotenv
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

load_dotenv(override=True)
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

llm = GoogleGenAI(
    model="models/gemini-1.5-pro"
)
Settings.llm = llm



st.title('Stockalyzer📈')
st.header('Nigerian Stock Analysis using LlamaIndex')


st.sidebar.header("Stock Samples from NGX")
for name, symbol in sample_stocks.items():
    st.sidebar.write(f"{name} ({symbol})")


report_type = st.selectbox('Select Analysis Type:', ['Stock Report', 'Competitor Analysis'])


if report_type == 'Stock Report':
    stock_symbol = st.text_input("Enter Stock Symbol:")
    if st.button("Generate Report") and stock_symbol:
        show_loading()

        prompt=single_stock_prompt(stock_symbol)
        #  prompt = single_stock_prompt.format(stock_symbol=stock_symbol)
        response = llm.complete(prompt)
        st.write(str(response))
        
        
        st.subheader("Stock Price Trend")
        st.error("Trend not available at this moment")


        # data = fetch_simulated_stock_data(stock_symbol)
        # data['Date'] = pd.to_datetime(data['Date'])
        # fig, ax = plt.subplots()
        # ax.plot(data['Date'], data['Price'], label='Price', color='blue')
        # ax.set_xlabel("Date")
        # ax.set_ylabel("Price")
        # ax.set_title(f"({stock_symbol}) Price Trend")
        # ax.legend()
        # st.pyplot(fig)
        

elif report_type == 'Competitor Analysis':

    stock_symbol_1 = st.text_input("Enter First Stock Symbol:")
    stock_symbol_2 = st.text_input("Enter Second Stock Symbol:")
    if st.button("Generate Report") and  stock_symbol_1 and stock_symbol_2:
        show_loading()

        prompt =competitor_analysis_prompt(stock_symbol_1, stock_symbol_2)
        response = llm.complete(prompt)
        st.write(str(response))

       
