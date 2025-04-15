# **OCCAM'S ADVISORY INC. Q&A ASSISTANT**

This project enables intelligent question answering strictly related to **Occam's Advisory Inc.**, leveraging Google Gemini API. It uses a layered architecture involving:

- **HTML Frontend** for user input
- **Node.js Middleware Server** for request handling and routing
- **FastAPI Backend** for relevance filtering and question answering via Gemini

---
## **Overview**

The **OCCAM'S ADVISORY INC. Q&A ASSISTANT** leverages a **RAG (Retrieve and Generate)**-like approach to provide accurate and relevant answers to user questions related to **Occam's Advisory Inc.**. This assistant integrates external data with generative models to create context-aware responses.

## **How It Works:**

1. **Data Collection (data.txt)**  
   Relevant information about Occam's Advisory Inc. is stored in a file called `data.txt`. This file includes essential details like business operations, company history, services, and frequently asked questions. This static knowledge base provides crucial context for answering questions.

2. **Relevance Check**  
   When a user sends a question, the system first checks if the question pertains to Occam's Advisory Inc. using a keyword-based relevance check. If the question is deemed relevant, the assistant proceeds to the next step.

3. **Prompt Generation**  
   A **base prompt** is generated that includes the content from `data.txt`. This allows the system to supply a well-rounded and contextualized response based on the company's information.

4. **Embedding Data into the Prompt**  
   The contents of the `data.txt` file are embedded into the prompt as additional context. This enriches the model’s understanding and enhances the accuracy of the generated response.

5. **Model Query and Response Generation**  
   The generative model (using the **Gemini API**) processes the enriched prompt and generates a response that provides an answer to the user’s question.

6. **Return the Answer**  
   The final answer is returned to the user, with the response generated based on the combination of static data from `data.txt` and the dynamic query from the user.

## **Key Flow:**

1. **User Query → Data Relevance Check → Is the query related to Occam's Advisory Inc.?**
   - **Yes** → Proceed to the next step.
   - **No** → Return a default response:  
     _"Sorry, I can only answer questions related to Occam's Advisory Inc."_

2. **Data from `data.txt` + User Query → Formulate Prompt for Model**  
3. **Send Prompt to Generative Model**  
4. **Model Generates Answer → Return Answer to User**

## **Benefits of the RAG-like Approach:**

- **Contextual Relevance**: By embedding relevant information from `data.txt`, the assistant can provide more accurate answers based on the company’s knowledge.
- **Efficient Knowledge Retrieval**: The system uses static knowledge from `data.txt` and combines it dynamically with user queries for improved responses.
- **Scalable and Extensible**: The system can be easily updated with new information in the `data.txt` file to ensure continuous improvement in answering questions.

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
- We can add support for file-based grounding or document search in `/rag`.

---
![Screenshot 2025-04-15 235239](https://github.com/user-attachments/assets/c1faf426-1164-4a59-9e31-52b32c1059a2)
![Screenshot 2025-04-15 235304](https://github.com/user-attachments/assets/e49d8d54-2346-4a14-9db7-f4b3351e3478)
![Screenshot 2025-04-15 235332](https://github.com/user-attachments/assets/a1045b27-8f42-44e2-aeea-22d5723318f1)

