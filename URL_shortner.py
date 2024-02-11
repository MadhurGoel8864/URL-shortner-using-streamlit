import streamlit as st
import pyshorteners as pyshrt
import pyperclip as pc
st.title("URL Shortner")
form = st.form("Name")

def cpying():
    pc.copy(shorted_URL)

url = form.text_input("Write URL here")
btn = form.form_submit_button("Get short URL")
shortner = pyshrt.Shortener()
if btn:
    shorted_URL = shortner.tinyurl.short(url)
    st.title("You shortes URL is here: ")
    st.write(shorted_URL)
    st.button("Copy", on_click=cpying())
    
        # cpying()
        # pc.copy(shorted_URL)

