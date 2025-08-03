

import streamlit as st
import requests
import pyperclip

st.title("AI Email Reply Generator")

# Input fields
subject = st.text_input("Email Subject", placeholder="e.g. Termination Notice")
email = st.text_area("Received Email", placeholder="Paste the email here")
role = st.selectbox("Your Role", ["project manager", "software engineer", "marketing lead"])
tone = st.selectbox("Preferred Tone", ["formal", "casual", "assertive"])


# Summarize received email
if st.button("Summarize received email"):
    if not email:
        st.warning("Please enter the received email to summarize.")
    else:
        try:
            summary_payload = {"email": email}
            summary_response = requests.post("http://127.0.0.1:8000/summarize-email/", json=summary_payload)
            if summary_response.status_code == 200:
                summary = summary_response.json()["summary"]
                st.success("Email Summary:")
                st.text_area("Summary", summary, height=100)
            else:
                st.error(f"Error: {summary_response.status_code} - {summary_response.json().get('detail')}")
        except requests.exceptions.ConnectionError:
            st.error("Backend not running. Please start the FastAPI server.")

# Button to submit
if st.button("Generate Reply"):
    if not subject or not email:
        st.warning("Subject and email are required.")
    else:
        payload = {
            "subject": subject,
            "email": email,
            "role": role,
            "tone": tone
        }
        try:
            response = requests.post("http://127.0.0.1:8000/generate-reply/", json=payload)
            if response.status_code == 200:
                reply = response.json()["reply"]
                st.success("AI-Generated Reply:")
                st.text_area("Reply", reply, height=200)
                st.button("Copy Reply", on_click=lambda: pyperclip.copy(reply))
            else:
                st.error(f"Error: {response.status_code} - {response.json().get('detail')}")
        except requests.exceptions.ConnectionError:
            st.error("Backend not running. Please start the FastAPI server.")
