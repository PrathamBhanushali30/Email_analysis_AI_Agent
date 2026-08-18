import streamlit as st
import json
import os

st.set_page_config(page_title="AI Email Security Dashboard", page_icon="🛡️")

st.title("🛡️ AI SOC Analyst Dashboard")
st.markdown("Monitoring inbox with CrewAI, VirusTotal, and Gemini.")

log_file = "logs.json"

if os.path.exists(log_file):
    try:
        with open(log_file, "r") as f:
            data = json.load(f)

        # Loop through the logs in reverse order (newest first)
        for entry in data[::-1]:
            st.subheader("Email Body")
            # If the email is empty or just whitespace, print a placeholder
            email_text = entry.get("email", "").strip()
            if email_text:
                st.info(email_text[:500])
            else:
                st.info("[No text in email body]")

            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("URL Scan Results")
                if entry.get("url_analysis"):
                    st.write(entry["url_analysis"])
                else:
                    st.write("No URLs found.")

            with col2:
                st.subheader("File Scan Results")
                if entry.get("file_analysis"):
                    st.write(entry["file_analysis"])
                else:
                    st.write("No attachments found.")

            st.subheader("Final SOC Verdict")
            # Display the CrewAI output nicely
            st.error(entry.get("final", "No final verdict available."))

            st.divider()
            
    except json.JSONDecodeError:
        st.warning("Log file is corrupted or empty. Waiting for new data...")
else:
    st.write("No data yet... send a test email to begin!")