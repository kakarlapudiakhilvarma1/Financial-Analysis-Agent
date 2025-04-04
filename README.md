# 💹 Financial Analysis Assistant

An AI-powered stock market analyst that fits in your browser.

This app uses the power of **Generative AI (Gemini via AGNO Agent)** and **real-time financial data** from **Yahoo Finance** to generate professional-grade analysis reports for any public stock ticker — instantly.

Built with **Streamlit** and driven by a well-instructed LLM agent, it emulates a **Wall Street analyst**, producing reports that include financial metrics, trends, analyst recommendations, and even future outlooks — all wrapped in a clean, interactive UI.

---

## 🚀 Why This App?

Investment research is often:
- Time-consuming 🕒
- Complex 📊
- Full of jargon 😵

**Financial Analysis Assistant** simplifies all of that. With just a stock symbol (like `AAPL`), the app:
- Fetches the latest market data
- Breaks it down with AI-generated insights
- Presents everything in a structured, readable report — with emojis for trend indicators too! 📈📉

---

## 🧠 How It Works

Under the hood:
- **LangChain-style Agent** using [AGNO](https://github.com/withagnos/agno) and Google **Gemini**
- **Live financial data** from Yahoo Finance via `YFinanceTools`
- Structured instructions to emulate a **professional analyst's mindset**
- Interactive frontend built with **Streamlit**

---

## 🛠️ Features

✔️ Executive summaries  
✔️ Analyst recommendations & ratings  
✔️ Stock fundamentals & financial metrics  
✔️ Real-time price & market trends  
✔️ Emoji trend indicators for clarity  
✔️ Forward-looking AI-powered outlook  
✔️ Easy-to-use web interface  

---

## 🧰 Setup Instructions

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/financial-analysis-agent.git
cd financial-analysis-agent
```

### 2. Create Env & Install Dependencies
```bash
conda create -p myenv python==3.10 -y
```

```bash
conda activate myenv/
```
#### requirements.txt
```bash
python-dotenv
agno
streamlit
google-genai
yfinance
```
```bash
pip install -r requirements.txt
```

### 3. Configure API Key

Create a `.env` file and set your Google Gemini API Key:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

If the `.env` is missing or empty, the app will securely prompt you for the key in the browser before launching.

---

## ▶️ Run the App
```bash
cd src
```
```bash
streamlit run 3_financial_agent_app_with_apikey_check.py
```

Then open your browser and go to: [http://localhost:8501](http://localhost:8501)

---

## 📷 UI Preview

*(Add screenshot or GIF here if possible for visual impact)*

---

## 🧪 Example Usage

1. Enter a stock symbol like `AAPL`
2. Click **Analyze**
3. Get a full AI-generated breakdown of the company’s performance

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Made with ❤️ using Streamlit, Gemini, AGNO Agents, and financial nerdiness.
```

---
