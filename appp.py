import streamlit as st
import speech_recognition as sr
import tempfile

st.title("Speech to Text App")

uploaded_file = st.file_uploader("Upload audio file", type=["wav"])

if uploaded_file is not None:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        temp_audio = tmp.name

    r = sr.Recognizer()

    with sr.AudioFile(temp_audio) as source:
        audio = r.record(source)

    try:
        text = r.recognize_google(audio)
        st.success("Text: " + text)
    except:
        st.error("Could not recognize audio")
