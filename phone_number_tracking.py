import streamlit as st
import phonenumbers
from phonenumbers import geocoder

# --- Custom CSS for background and styling ---
st.markdown(
    """
    <style>
    body {
        background-color: #23272F;
    }
    .big-title {
        font-size: 3em;
        font-weight: bold;
        color: #F9B17A;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subtitle {
        font-size: 1.3em;
        color: #9BA4B5;
        text-align: center;
        margin-bottom: 2em;
    }
    .card {
        background: #1B1F27;
        border-radius: 18px;
        padding: 2em 2em 1em 2em;
        box-shadow: 0 6px 30px rgba(0,0,0,0.23);
        margin-bottom: 2em;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- Header Image ---
st.image("52c6bdf7-5c03-463b-8f15-16c9aadfb4e8.png.png", use_column_width=True)

# --- Title and subtitle ---
st.markdown('<div class="big-title">📞 Phone Number Geolocator</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Find out which country a phone number is from!<br>Enter phone numbers below (with country code, e.g. +919544357866)</div>',
    unsafe_allow_html=True
)

# --- User input in a card ---
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    phone_numbers = st.text_area("Paste phone numbers here (one per line):", height=100)
    st.markdown('</div>', unsafe_allow_html=True)

# --- Process numbers and display results ---
if st.button("🔍 Find Locations"):
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 🌍 Results")
    if phone_numbers.strip() == "":
        st.info("Please enter at least one phone number above.")
    else:
        lines = phone_numbers.strip().split("\n")
        found = False
        for number in lines:
            try:
                pn = phonenumbers.parse(number)
                location = geocoder.description_for_number(pn, "en")
                if location:
                    st.success(f"**{number.strip()}**: {location}")
                    found = True
                else:
                    st.warning(f"**{number.strip()}**: Country not found. Please check the number.")
            except Exception:
                st.error(f"**{number.strip()}**: Invalid or incomplete number. Example: +919544357866")
        if not found:
            st.info("No valid phone numbers found.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- Friendly Footer ---
st.markdown(
    """
    <hr>
    <div style='text-align:center; color:#555; font-size:1em; margin-top:2em;'>
        Made with ❤️ using Streamlit
    </div>
    """,
    unsafe_allow_html=True
)
