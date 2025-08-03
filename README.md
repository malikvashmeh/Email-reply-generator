# AI Email Reply Generator

A simple web app that generates AI-powered email replies using Streamlit (frontend) and FastAPI (backend) with Google Gemini API.

## Requirements

- Python 3.8+
- pip
- Google API Key (for Gemini)

## Python Packages
- streamlit
- requests
- fastapi
- uvicorn
- python-dotenv
- google-generativeai

## Setup

1. Clone the repository and navigate to the project folder.
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install streamlit requests fastapi uvicorn python-dotenv google-generativeai
   ```
4. Create a `.env` file and add your Google API key:
   ```env
   GOOGLE_API_KEY=your_api_key_here
   ```
5. Start the FastAPI backend:
   ```bash
   uvicorn main:app --reload
   ```
   If you see an error like `[Errno 98] Address already in use`, stop any running server or use a different port:
   ```bash
   uvicorn main:app --reload --port 8001
   ```
6. In a new terminal, start the Streamlit frontend:
   ```bash
   streamlit run app.py
   ```

## Usage
- Open the Streamlit app in your browser (usually at http://localhost:8501)
- Enter the email subject, received email, your role, and preferred tone
- Click "Generate Reply" to get an AI-generated response

## Notes
- The backend uses the Gemini model: `models/gemini-2.5-pro` for best results.
- If you get a 500 error from the frontend, make sure your backend is running and your Google API key is valid.

---
