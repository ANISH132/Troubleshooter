# Tech Issue Assistant

A Streamlit web application that uses Groq LLM API to provide step-by-step solutions for technical issues.

## Features

- **User-friendly Interface**: Simple text input for describing technical issues
- **AI-Powered Solutions**: Uses Groq's Llama 3 model to generate clear, actionable solutions
- **No Links Required**: Provides detailed explanations instead of just links
- **Real-time Processing**: Instant responses to user queries

## Setup

### Prerequisites

- Python 3.7+
- Groq API key

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd HealthCheck
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
   ```
   GROQ_API_KEY=your-actual-groq-api-key-here
   ```
   
   Or set it directly in the code (not recommended for production):
   ```python
   GROQ_API_KEY = "your-actual-groq-api-key-here"
   ```

4. **Run the application**
   ```bash
   streamlit run troubleshooter.py
   ```

5. **Access the app**
   
   Open your browser and go to: `http://localhost:8501`

## Usage

1. Enter your technical issue in the text area
2. Click "Get Solution"
3. Wait for the AI to generate a step-by-step solution
4. Follow the provided instructions

## Example

**Input**: "My cursor is stuck"
**Output**: "Please force shutdown the device by pressing and holding the power button for 40 seconds. Turn it on again and check its status."

## Technologies Used

- **Streamlit**: Web application framework
- **Groq API**: LLM service for generating solutions
- **Python**: Backend programming language
- **Requests**: HTTP library for API calls

## API Configuration

This application uses Groq's API with the `llama3-8b-8192` model. The API provides:
- Fast response times
- High-quality solutions
- Free tier available (1000 requests/day)

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE). 