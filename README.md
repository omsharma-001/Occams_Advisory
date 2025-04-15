Occam's Advisory Inc. Q&A Assistant

This project enables intelligent question answering strictly related to **Occam's Advisory Inc.**, leveraging Google Gemini API. It uses a layered architecture involving:

- **HTML Frontend** for user input
- **Node.js Middleware Server** for request handling and routing
- **FastAPI Backend** for relevance filtering and question answering via Gemini

---

## 📐 Architecture Overview

```text
+-----------------+       +-------------------+       +--------------------------+
|     Frontend    | --->  |   Node.js Server  | --->  |  FastAPI + Gemini API   |
|  (HTML/JS/CSS)  |       | (Express/HTTP)    |       | (Relevance Filtering,   |
|                 | <---  |                   | <---  |   Gemini Integration)   |
+-----------------+       +-------------------+       +--------------------------+
```

---

## 💡 Features

- ✅ CORS-enabled FastAPI backend
- ✅ Strict relevance filtering (Only answers questions about Occam’s Advisory Inc.)
- ✅ Uses Gemini 2.0 Flash for generating answers
- ✅ Configurable hyperparameters (temperature, topK, topP)
- ✅ Node.js as a routing layer between HTML frontend and Python backend

---

## 🔧 Tech Stack

- **Frontend:** HTML + JS (optional framework)
- **Middleware:** Node.js (Express.js)
- **Backend:** Python 3 + FastAPI + Gemini API
- **Language Model:** Gemini 2.0 Flash

---

## 🚀 How to Run

### 1. Start the FastAPI backend

```bash
python -m uvicorn rag_api:app --host 127.0.0.1 --port 8000
```

### 2. Start the Node.js server

```bash
node index.js
```

### 3. Open the Frontend

Launch `index.html` in your browser by clicking the url obtained after running "node index.js" command.
http://localhost:3000
---

## 🌐 API Endpoints

### POST `/ask` (via FastAPI)

- **Request Body:**
```json
{
  "question": "What services does Occam's Advisory Inc. provide?"
}
```

- **Response:**
```json
{
  "answer": "Occam's Advisory Inc. provides data-driven advisory services in the finance and analytics domains..."
}
```

## 📌 Notes

- Used Customize `data.txt` to simulate RAG-like behavior.
- You can add support for file-based grounding or document search in `/rag`.

---
