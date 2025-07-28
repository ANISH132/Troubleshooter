import streamlit as st
import requests
import os
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# Set your Groq API key from environment variable or .env file
GROQ_API_KEY = "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"

st.title("Tech Issue Assistant")
st.markdown("Describe your technical issue and get a step-by-step solution.")

# User input
user_issue = st.text_area("Describe your issue:", placeholder="e.g., My cursor is stuck, My computer is running slow, etc.")

if user_issue:
    if st.button("Get Solution"):
        with st.spinner("Finding a solution..."):
            try:
                headers = {
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                }
                
                data = {
                    "model": "llama3-8b-8192",
                    "messages": [
                        {
                            "role": "system",
                            "content": "You are a helpful technical assistant. When a user describes a technical issue, provide a clear, step-by-step solution in plain language. Avoid providing links; instead, explain the fix in detail. Make the solution easy to follow and actionable."
                        },
                        {
                            "role": "user",
                            "content": f"User Issue: {user_issue}"
                        }
                    ],
                    "max_tokens": 300,
                    "temperature": 0.7
                }
                
                response = requests.post(
                    "https://api.groq.com/openai/v1/chat/completions",
                    headers=headers,
                    json=data
                )
                
                if response.status_code == 200:
                    solution = response.json()["choices"][0]["message"]["content"].strip()
                    st.success("**Solution:**")
                    st.write(solution)
                else:
                    st.error(f"API Error: {response.status_code} - {response.text}")
                
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Please check if your Groq API key is set correctly.")
else:
    st.info("Enter your technical issue above to get started.") 