# 🌐 Universal Converter App (Streamlit)

A powerful, all-in-one **unit converter** web app built using **Streamlit** that can convert between:

- 📏 Length
- ⚖️ Weight
- 🌡️ Temperature
- 💰 Currency (real-time exchange rates via API)

---

## 🎯 Features

- 🔁 Intuitive dropdown-based unit selection
- 🎛️ Real-time conversion results
- 💸 Live currency rates powered by [ExchangeRate-API](https://www.exchangerate-api.com/)
- 🎈 Balloons animation on successful conversion
- 🧠 Smart logic for all supported conversions

---

## 🛠 Tech Stack

- **Python 3.x**
- **Streamlit** – UI framework
- **Requests** – For currency API fetching

---

## 🚀 How to Run Locally

### 1. Install dependencies
```bash
pip install streamlit requests

2. Save your script (e.g., universal_converter.py)
3. Run the app

streamlit run universal_converter.py

🔢 Supported Units
📏 Length

    Meters

    Kilometers

    Miles

    Feet

⚖️ Weight

    Kilograms

    Grams

    Pounds

    Ounces

🌡️ Temperature

    Celsius

    Fahrenheit

    Kelvin

💰 Currency

    Real-time exchange rates with all currencies supported by ExchangeRate-API (base: USD)

💡 Example Use

    Convert 10 Kilograms to Pounds
    ✅ 10 Kilograms = 22.05 Pounds

    Convert 100 USD to EUR
    ✅ 100 USD = 91.30 EUR (based on live rate)

🌐 API Info

    Source: ExchangeRate-API.com

    Base Currency: USD

    ⚠️ Ensure you have a stable internet connection to fetch live rates

📌 Improvements You Can Add

    Input validation for negative or invalid values

    Caching exchange rate responses for performance

    Offline fallback rates or local JSON

    More units (e.g., Time, Area, Volume)

📄 License

This project is open source under the MIT License.
