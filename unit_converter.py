import streamlit as st

# Conversion Factors
conversion_factors = {
    "length": {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "inches": 39.3701,
        "feet": 3.28084,
        "yards": 1.09361,
        "miles": 0.000621371
    },
    "weight": {
        "kilograms": 1,
        "grams": 1000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
}

# Function to convert units
def convert_units(value, from_unit, to_unit, unit_type):
    if unit_type in ["length", "weight"]:
        return value * (conversion_factors[unit_type][to_unit] / conversion_factors[unit_type][from_unit])
    elif unit_type == "temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
    return None

# Streamlit UI
st.title("Unit Converter")

unit_type = st.selectbox("Select Unit Type", ["length", "weight", "temperature"])

if unit_type == "temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit"])
    to_unit = "Fahrenheit" if from_unit == "Celsius" else "Celsius"
    value = st.number_input(f"Enter {from_unit} value", format="%.2f")
else:
    units = list(conversion_factors[unit_type].keys())
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input(f"Enter {from_unit} value", format="%.2f")

if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, unit_type)
    if result is not None:
        st.success(f"Converted Value: {result:.2f} {to_unit}")
    else:
        st.error("Invalid conversion")
