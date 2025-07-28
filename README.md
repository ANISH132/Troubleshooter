# Tech Issue Assistant

A Streamlit web application that helps users troubleshoot technical issues using AI-powered solutions.

## Features

- Describe technical issues in plain language
- Get step-by-step solutions powered by Groq AI
- Simple and intuitive interface

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up your API key:
   - **For local development:** Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and add your actual Groq API key
   - **For deployment:** Set the `GROQ_API_KEY` secret in your hosting platform

3. Run the app:
```bash
streamlit run troubleshooter.py
```

## Deployment

This app can be deployed on:
- Streamlit Cloud (recommended)
- Heroku
- Railway
- Render

See deployment instructions in the documentation. 