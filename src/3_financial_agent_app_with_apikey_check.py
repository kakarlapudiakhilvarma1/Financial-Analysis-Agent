from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.yfinance import YFinanceTools
from textwrap import dedent
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initially try to get the API key from the environment
api_key = os.getenv("GOOGLE_API_KEY")

# Define the financial analysis agent
finance_agent = Agent(
    model=Gemini(id="gemini-2.0-flash-exp"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            historical_prices=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=dedent("""\
        You are a seasoned Wall Street analyst with deep expertise in market analysis! 📊
        Follow these steps for comprehensive financial analysis:
        1. Market Overview
           - Latest stock price
           - 52-week high and low
        2. Financial Deep Dive
           - Key metrics (P/E, Market Cap, EPS)
        3. Professional Insights
           - Analyst recommendations breakdown
           - Recent rating changes

        4. Market Context
           - Industry trends and positioning
           - Competitive analysis
           - Market sentiment indicators

        Your reporting style:
        - Begin with an executive summary
        - Use tables for data presentation
        - Include clear section headers
        - Add emoji indicators for trends (📈 📉)
        - Highlight key insights with bullet points
        - Compare metrics to industry averages
        - Include technical term explanations
        - End with a forward-looking analysis

        Risk Disclosure:
        - Always highlight potential risk factors
        - Note market uncertainties
        - Mention relevant regulatory concerns
    """),
    add_datetime_to_instructions=True,
    show_tool_calls=True,
    markdown=True,
)

# Inject custom CSS to create a scrollable area
st.markdown("""
    <style>
    .scrollable {
        height: 400px;
        overflow-y: scroll;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI setup
st.title("Financial Analysis Assistant")

# Sidebar content for user guidance
with st.sidebar:
    st.header("📘 How to Use")
    st.markdown(
        """
        This AI-powered **Financial Analysis Assistant** helps you analyze stocks using live market data.  
        Simply:
        1. Enter a **stock ticker symbol** (e.g., `AAPL`, `GOOGL`, `TSLA`)
        2. Click **"Analyze"**
        3. Get a detailed report with 📈 trends, 🧾 financials, and 🔍 analyst insights.

        ---
        """
    )

    st.subheader("💡 Examples")
    st.markdown(
        """
        - `AAPL` – Apple Inc.  
        - `MSFT` – Microsoft Corp  
        - `GOOGL` – Alphabet Inc  
        - `TSLA` – Tesla Inc  
        - `NFLX` – Netflix Inc  
        """
    )

    st.subheader("🔐 Notes")
    st.markdown(
        """
        - Data is pulled live using [Yahoo Finance](https://finance.yahoo.com).
        - Powered by **Gemini** via AGNO Agent framework.
        - Ensure your API keys are configured properly.
        """
    )

    st.markdown("---")
    #st.caption("Made with ❤️ using Streamlit, Agno Agents, and Gemini.")

# Input field for the API key if not set
if not api_key:
    api_key = st.sidebar.text_input("Enter your API key:")
    if api_key:
        os.environ["GOOGLE_API_KEY"] = api_key
    else:
        st.sidebar.warning("API key is required to analyze stocks.")

# Input field for the stock ticker
ticker = st.text_input("Enter the stock ticker symbol (e.g., AAPL):")

# Button for triggering analysis
if st.button("Analyze"):
    if ticker and api_key:
        query = f"What's the latest news and financial performance of {ticker}?"
        with st.spinner("Analyzing..."):
            response = finance_agent.run(query, stream=False)
        if response and response.content:
            st.subheader("Analysis Report:")
            # Use custom scrollable div for the response content
            st.markdown(f'<div class="scrollable">{response.content}</div>', unsafe_allow_html=True)
        else:
            st.error("No response received from the agent.")
    else:
        if not ticker:
            st.error("Please enter a stock ticker symbol.")
        if not api_key:
            st.error("API key is required to proceed.")
