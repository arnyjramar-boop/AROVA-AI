import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

app = FastAPI()

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

class ChatMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(data: ChatMessage):
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions="You are AROVA, a helpful AI assistant.",
        input=data.message
    )

    return {"reply": response.output_text}

app.mount(
    "/",
    StaticFiles(directory="static", html=True),
    name="static"
)