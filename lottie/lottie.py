import streamlit as st
from streamlit_lottie import st_lottie
import requests
import time

# Function to load Lottie animations from a URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load multiple Lottie animations from URLs
animation_1 = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_0pivj3sk.json')  # Example animation
animation_2 = load_lottieurl('https://assets9.lottiefiles.com/packages/lf20_w51pcehl.json')  # Another animation

# Sidebar for user options
st.sidebar.title("Interactive Lottie Animations")
refresh_app = st.sidebar.button("Refresh App")
trigger_animation = st.sidebar.button("Trigger Animation")

# Displaying multiple Lottie animations with conditions
st.title("Creative Streamlit-Lottie App")
if animation_1:
    st_lottie(animation_1, key="main", height=300)

# Triggering different animations based on button interaction
if trigger_animation and animation_2:
    st_lottie(animation_2, key="triggered", height=300)
    st.success("Animation Triggered! 🎉")

# Rerun app on condition
if refresh_app:
    time.sleep(1)
    st.rerun()

# Show the second animation only during certain hours
current_hour = time.localtime().tm_hour
if 6 <= current_hour <= 18:  # Show during daytime
    st.write("Daytime Mode")
    if animation_2:
        st_lottie(animation_2, height=300)
else:
    st.write("Nighttime Mode - Animation Paused")

st.write("Customize interactions in the sidebar to refresh or trigger animations.")
