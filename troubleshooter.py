import streamlit as st
import requests
import os
# from dotenv import load_dotenv

# Load environment variables from .env file
# load_dotenv()

# Set your Groq API key from environment variable or .env file
# GROQ_API_KEY = os.getenv("GROQ_API_KEY", "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")
GROQ_API_KEY = "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"

st.title("🔧 Tech Issue Assistant")
st.markdown("Describe your technical issue and get a step-by-step solution.")

# User input
user_issue = st.text_area("Describe your issue:", placeholder="e.g., My cursor is stuck, My computer is running slow, etc.", height=120)

# Create columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    submit_button = st.button("🚀 Get Solution", type="primary", use_container_width=True)

if user_issue and submit_button:
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
                    
                    # Create a nice solution display
                    st.markdown("---")
                    st.markdown("### 💡 **Solution Found!**")
                    
                    # Display solution in a nice container
                    with st.container():
                        st.markdown(f"""
                        <div style="
                            background-color: #f0f2f6;
                            padding: 20px;
                            border-radius: 10px;
                            border-left: 4px solid #00ff88;
                            margin: 10px 0;
                        ">
                        {solution}
                        </div>
                        """, unsafe_allow_html=True)
                    
                    # Add a copy button
                    st.button("📋 Copy Solution", on_click=lambda: st.write("Solution copied to clipboard!"))
                    
                else:
                    st.error(f"❌ API Error: {response.status_code} - {response.text}")
                
            except Exception as e:
                st.error(f"❌ Error: {e}")
                st.info("🔑 Please check if your Groq API key is set correctly.")
else:
    if not user_issue:
        st.info("💡 Enter your technical issue above to get started.")
    elif not submit_button:
        st.info("🚀 Click the 'Get Solution' button to proceed.") 
