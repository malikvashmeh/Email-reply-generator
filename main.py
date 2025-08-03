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