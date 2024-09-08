import streamlit as st
import random
from datetime import datetime, timedelta
import markdown

# 💡 Jupyterlite
st.header("💡 Jupyterlite Demo")
st.title("Jupyterlite Demo")
st.write("This app demonstrates the usage of various modules.")

# ⌨️ Keyboard text
st.header("⌨️ Keyboard text")
keyboard_input = st.text_input("Enter some text:")
st.write("You entered:", keyboard_input)

# 🎯 Keyboard to URL
st.header("🎯 Keyboard to URL")
url_input = st.text_input("Enter URL:")
if url_input:
    st.write(f"[Click here to visit]({url_input})")

# 🌧️ Let emojis rain
st.header("🌧️ Let emojis rain")
if st.button("Let Emojis Rain"):
    emojis = ["🌧️", "☔", "🌈", "🌦️", "⛅"]
    for _ in range(10):
        st.write(random.choice(emojis))

# 📅 Mandatory Date Range Picker
st.header("📅 Mandatory Date Range Picker")
date_range = st.date_input("Select a date range", [datetime.today(), datetime.today() + timedelta(days=1)])
st.write(f"Selected range: {date_range}")

# 〽️ Markdownlit
st.header("〽️ Markdown")
markdown_text = "# This is a markdown title"
st.markdown(markdown.markdown(markdown_text))

# 🫵 Mentions
st.header("🫵 Mentions")
mention = st.text_input("Mention someone", "@username")
st.write(f"You mentioned: {mention}")

# ♠️ Metric Cards
st.header("♠️ Metric Cards")
st.metric(label="Current Temperature", value="23 °C", delta="-2 °C")

# 🗳️ No-Default Selectbox
st.header("🗳️ No-Default Selectbox")
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"], index=0)
st.write(f"Selected: {option}")

# 📊 Prometheus (Example using a simple counter)
st.header("📊 Prometheus (Counter Example)")
counter = st.number_input("Counter", 0, 100, step=1)
st.write(f"Counter: {counter}")

# 🟰 Row Layout
st.header("🟰 Row Layout")
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")

# 📦 Stlite Sandbox (Incorporating stlite)
st.header("📦 Stlite Sandbox")
st.write("Stlite sandbox is integrated.")

# 🔑 Keyup text input
st.header("🔑 Keyup text input")
keyup_input = st.text_input("Type and see live:", "")
st.write(f"Keyup: {keyup_input}")

# 🔛 Stateful Button
st.header("🔛 Stateful Button")
if st.button("Click me"):
    st.write("Button clicked!")

# 💬 Stateful Chat
st.header("💬 Stateful Chat")
chat_input = st.text_input("Chat here:", "")
if st.button("Send"):
    st.write(f"Sent: {chat_input}")

# ✔️ To-do items
st.header("✔️ To-do items")
todo = st.text_area("To-Do List")
st.write("Your tasks:", todo.splitlines())

# ➡️ Toggle button
st.header("➡️ Toggle button")
toggle = st.checkbox("Toggle")
st.write(f"Toggle is {'On' if toggle else 'Off'}")

# 🌊 Streaming Write
st.header("🌊 Streaming Write")
if st.button("Start Streaming"):
    st.write("Stream started.")

# 🎨 Styleable Container
st.header("🎨 Styleable Container")
with st.container():
    st.write("This is a container with style.")

# 🖱️ Switch page function
st.header("🖱️ Switch page function")
if st.button("Go to the next page"):
    st.write("Page switched.")

# 🔖 Tags
st.header("🔖 Tags")
tags = st.text_input("Enter tags (comma separated):")
st.write("Tags:", tags.split(','))

# 🌗 Theme
st.header("🌗 Theme")
theme = st.selectbox("Choose a theme", ["Light", "Dark"])
st.write(f"Selected theme: {theme}")

# 🔛 Toggle Switch
st.header("🔛 Toggle Switch")
toggle_switch = st.checkbox("Toggle Switch")
st.write(f"Switch is {'On' if toggle_switch else 'Off'}")

# 🎚 Vertical Slider
st.header("🎚 Vertical Slider")
vertical_slider = st.slider("Vertical Slider", 0, 100, 50)
st.write(f"Slider value: {vertical_slider}")

# ❗ Word importances
st.header("❗ Word importances")
words = st.text_area("Enter words to highlight:")
st.write("Word importances highlighted:", words.split())
