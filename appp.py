import streamlit as st
import speech_recognition as sr

st.title("Voice to Text App")

r = sr.Recognizer()

if st.button("Start Recording"):
    with sr.Microphone() as source:
        st.write("Speak now...")
        audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            st.success("You said: " + text)
        except:
            st.error("Sorry, could not understand.")