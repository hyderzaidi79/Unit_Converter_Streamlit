import streamlit as st
import requests

def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Miles": 0.000621371,
        "Feet": 3.28084
    }
    return value * length_units[to_unit] / length_units[from_unit]

def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    return data.get("rates", {})

def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency == "USD":
        return amount * rates.get(to_currency, 1)
    elif to_currency == "USD":
        return amount / rates.get(from_currency, 1)
    else:
        return amount * (rates.get(to_currency, 1) / rates.get(from_currency, 1))
        
rates = get_exchange_rates()
currencies = list(rates.keys())

st.title("📏⚖️🌡️💰 Universal Converter")

conversion_type = st.selectbox("Choose Conversion Type:", ["Length", "Weight", "Temperature", "Currency"])

if conversion_type == "Length":
    units = ["Meters", "Kilometers", "Miles", "Feet"]
    convert_func = convert_length
elif conversion_type == "Weight":
    units = ["Kilograms", "Grams", "Pounds", "Ounces"]
    convert_func = convert_weight
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    convert_func = convert_temperature
elif conversion_type == "Currency":
    units = currencies
    convert_func = lambda amount, from_currency, to_currency: convert_currency(amount, from_currency, to_currency, rates)

value = st.number_input(f"Enter value to convert ({conversion_type}):", min_value=0.0, format="%.2f")
from_unit = st.selectbox("From:", units)
to_unit = st.selectbox("To:", units)

if st.button("Convert"):
    result = convert_func(value, from_unit, to_unit)
    st.success(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")
    st.balloons()
