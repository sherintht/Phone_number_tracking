pip install phonenumbers
import streamlit as st
import phonenumbers
from phonenumbers import geocoder

st.title("Phone Number Geolocator")

# You can let users enter numbers
phone_numbers = st.text_area(
    "Enter phone numbers (one per line, with country code, e.g. +919544357866):"
)

if st.button("Find Locations"):
    st.write("## Phone Numbers Location")
    lines = phone_numbers.strip().split("\n")
    for number in lines:
        try:
            pn = phonenumbers.parse(number)
            location = geocoder.description_for_number(pn, "en")
            st.write(f"**{number}**: {location}")
        except Exception as e:
            st.write(f"**{number}**: Invalid or unrecognized number.")
