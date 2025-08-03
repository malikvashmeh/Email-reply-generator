#front end 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from gemini import GeminiReplyGenerator

app = FastAPI()

# CORS middleware to allow requests from any origin

app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class EmailRequest(BaseModel):
    email: str
    role: str
    tone: str

#sumarize email request class
class EmailSummaryRequest(BaseModel):
    email: str


@app.post("/generate-reply/")
def generate_reply(data: EmailRequest):
    try:
        generator = GeminiReplyGenerator()
        reply = generator.generate_reply(
            email=data.email,
            role=data.role,
            tone=data.tone
        )
        return {"reply": reply}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Summarize email endpoint
@app.post("/summarize-email/")
def summarize_email(data: EmailSummaryRequest):
    try:
        generator = GeminiReplyGenerator()
        prompt = f"Summarize the following email in 2-3 sentences for a business context.\n\nEmail:\n{data.email}"
        summary = generator.model.generate_content(prompt).text.strip()
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))