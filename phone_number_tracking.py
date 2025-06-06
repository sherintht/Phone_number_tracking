import streamlit as st
import phonenumbers
from phonenumbers import geocoder

st.set_page_config(page_title="Phone Number Geolocator", page_icon=":telephone_receiver:", layout="wide")

# Banner image (replace with your actual filename as needed)
st.image("phone_number_loatoro_banner.png", use_container_width=True)

# Main title and subtitle (one header only, friendly and clear)
st.markdown(
    "<h1 style='text-align: center; color: #FF9F43; margin-bottom: 0.25em;'>📞 Phone Number Geolocator</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<div style='text-align: center; color: #888; font-size: 1.25em; margin-bottom: 2em;'>"
    "Easily find the country of any phone number. <br>"
    "Type or paste phone number(s) below (with country code, e.g. +919544357866), one per line."
    "</div>",
    unsafe_allow_html=True
)

# Phone number input (single, clear, and customer-friendly)
phone_numbers = st.text_area(
    "Type or paste phone number(s) below:",
    placeholder="+14155552671\n+919544357866",
    height=100
)

# Button with icon
if st.button("🔍 Find Locations"):
    st.markdown("<h3 style='color:#00B894;'>🌍 Results</h3>", unsafe_allow_html=True)
    if phone_numbers.strip() == "":
        st.info("Please enter at least one phone number above.")
    else:
        lines = [line.strip() for line in phone_numbers.strip().split("\n") if line.strip()]
        found = False
        for number in lines:
            try:
                pn = phonenumbers.parse(number)
                location = geocoder.description_for_number(pn, "en")
                if location:
                    st.success(f"**{number}** : {location}")
                    found = True
                else:
                    st.warning(f"**{number}** : Country not found. Please check the number.")
            except Exception:
                st.error(f"**{number}** : Invalid or incomplete number. Example: +919544357866")
        if not found:
            st.info("No valid phone numbers found.")

# Friendly footer
st.markdown(
    "<hr><div style='text-align:center; color:#BBB; font-size:1em; margin-top:2em;'>"
    "Made with ❤️ by your team. Powered by Streamlit."
    "</div>",
    unsafe_allow_html=True
)
