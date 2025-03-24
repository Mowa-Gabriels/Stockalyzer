
import streamlit as st
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def single_stock_prompt(stock_symbol):
    return f"""

        You are Stockalyzer, A Financial Analyst that solely  provides Nigerian  stocks information.
        Please provide a comprehensive breakdown of  {stock_symbol} from the perspective of a senior Wall Street financial analyst.
        
                1. Company Overview:
            - Describe the company’s primary business activities and market position.
            - Include any notable historical milestones.

            2. Historical Performance:
            - Summarize the stock’s past performance, key growth drivers, and any significant price movements.
            - Highlight important events that have influenced the stock's performance.

            3. Financial Health and Metrics:
            - Analyze key financial indicators such as revenue growth, profitability, liquidity, and debt levels.
            - Discuss operational efficiencies and any challenges the company faces.

            4. Market Environment and Industry Trends:
            - Describe the competitive landscape and relevant market trends.
            - Explain how macroeconomic factors or industry-specific risks might impact the stock.

            5. Forecast and Valuation:
            - Provide a forward-looking forecast based on public information and historical trends.
            - Discuss potential catalysts or headwinds for the stock.
            - Present key valuation metrics (e.g., P/E, P/B ratios) in context.

            6. Investment Recommendation:
            - Conclude with a clear recommendation if the investor should Buy, Hold, or Sell.
            - Explain the reasoning behind the recommendation, taking into account both risks and opportunities.

            Generate Tables as part of the response.

            The final result should be well-worded, logically structured, and easy to understand, delivering high-quality insights that would be useful to both professional and individual investors.
            
            
            Note: if the company is not registered on nigerian stock exchange, notify the user you can only give update on nigerian stocks
            """
        
     
    

def competitor_analysis_prompt(stock_symbol_1, stock_symbol_2):
    return  f"""

         You are Stockalyzer, A Financial Analyst that solely  provides Nigerian  stocks information. If any of the symbols or company provided is not on the 
         Nigerian stock exchange, kindly tell the user you only analyze nigerian stocks. however if it is a niverisn company that is registered
         on the  Nigerian Sto k exchange, proccs to give very detailed comparison.
        Compare ({stock_symbol_1}) and  ({stock_symbol_2}) from a financial and market perspective:
        
        1. Business Model and Market Position
        2. Historical Performance and Stock Trends
        3. Financial Metrics Comparison
        4. Competitive Advantages and Challenges
        5. Future Outlook and Industry Position
        6. Investment Recommendation

        Generate Tables, charts and graph as part of the response.
        
        Provide a well-structured and insightful comparison for investors.
        """
    


sample_stocks = {
    "Nigerian Breweries Plc": "NB",
"Dangote Cement Plc": "DANGCEM",
"MTN Nigeria Communications Plc": "MTNN",
"Guaranty Trust Holding Co Plc": "GTCO",
"Zenith Bank Plc": "ZENITHBANK",
"Nestlé Nigeria Plc": "NESTLE",
"FBN Holdings Plc": "FBNH",
"Access Holdings Plc": "ACCESSCORP",
"BUA Cement Plc": "BUACEMENT",
"Seplat Energy Plc": "SEPLAT",
"Transcorp Hotels Plc": "TRANSCORP"
}

loading_messages = [
    "Checking NGX database...",
    "Consulting the Naija oracle for stock wisdom...",
    "Stock memos loading—abeg hold tight...",
    "Caught up in Lagos holdup...",
    "Dialing up the Lagos hustle for market insights...",
    "Fetching that data faster than an Okada in Lagos...",
    "Peeping into the market like a true Naija oga...",
    "No shaking, insights are on the way...",
    "Sipping zobo while we crunch those numbers...",
     "Finally found data...",
    "Analyzing data...",
    "Making recommendation...",
    

]
def show_loading():
    for message in loading_messages:
        with st.spinner(message):
            time.sleep(3)

# def fetch_simulated_stock_data(stock_symbol):
#     """
#     Use the LLM to get generating historical stock data in CSV format.
#     Expected CSV format:
#        Date,Price
#        2025-01-01,100.5
#        2025-01-02,101.2
#        ...
#     """
#     prompt = (f"Generate a CSV with headers Date,Price containing REAL-TIME daily closing stock prices "
#               f"for the past 21 days for({stock_symbol}). "
#               "Use date format YYYY-MM-DD .")
#     response = llm.complete(prompt)
#     try:
#         df = pd.read_csv(io.StringIO(response))
#         return df
#     except Exception as e:
#         st.error("Error parsing CSV data from LLM response. Using fallback simulated data.")
#         # Fallback: generate dummy data
#         dates = pd.date_range(end=pd.Timestamp.today(), periods=100).tolist()
#         prices = np.cumsum(np.random.randn(100)) + 100
#         return pd.DataFrame({'Date': dates, 'Price': prices})

