import requests
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str

# Gemini API URL
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=AIzaSyAOCQixumleEuCR10Oft9kKEzrHyQewdy4"

def load_context_from_file(file_path: str = "data.txt") -> str:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "Context data is unavailable."

def generate_content_with_gemini(prompt: str, context: str = "") -> str:
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{context}\n\nBased on the above context, answer the following question:\n{prompt}"
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2,
            "topK": 50,
            "topP": 0.9,
            "maxOutputTokens": 512
        }
    }

    try:
        response = requests.post(GEMINI_URL, json=payload, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        data = response.json()
        if data.get("candidates"):
            parts = data["candidates"][0]["content"]["parts"]
            if parts:
                return parts[0].get("text", "No text content available")
        return "No content found in response from Gemini."
    except requests.exceptions.RequestException as e:
        print("Error calling Gemini API:", e)
        return "Error occurred while calling Gemini API."

def is_relevant_to_occams_advisory(question: str) -> bool:
    base_prompt = (
        "You are a helpful assistant specializing in answering questions about Occam's Advisory Inc.\n\n"
        "Your task is to determine whether the following question relates specifically to Occam's Advisory Inc.\n"
        "If the question relates to the company, answer 'yes'. If not, answer 'no'.\n\n"
        f"Question: {question}\n"
        "Answer only with 'yes' or 'no'."
    )
    response = generate_content_with_gemini(base_prompt)
    response = response.strip().lower()
    return response == "yes"

@app.post("/ask")
def ask_question(q: Question) -> Dict[str, str]:
    if not is_relevant_to_occams_advisory(q.question):
        return {"answer": "Sorry, I can only answer questions related to Occam's Advisory Inc."}

    context = load_context_from_file("data.txt")

    prompt = (
        f"{q.question}\n\n"
        "If the answer is not found in the provided context, reply: "
        "'Sorry, I don't have enough information to answer that based on the current context.'"
    )

    answer = generate_content_with_gemini(prompt, context=context)
    return {"answer": answer}

@app.post("/rag")
def ask_rag_stub(q: Question) -> Dict[str, str]:
    return {"answer": "RAG endpoint not implemented yet. Use /ask instead."}
