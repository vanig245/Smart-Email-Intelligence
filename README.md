# Smart Email Intelligence

A backend-focused FastAPI playground designed to practice user authentication, secure cookie session tracking, local JSON database interactions, and asynchronous AI chat orchestration using the Groq SDK.

> **DISCLAIMER:** This project is built entirely for the purpose of **Backend Development & FastAPI practice**. The core focus is strictly on architecture, security routing, request validation, and API data flows. The frontend is a minimal, functional sandbox interface meant purely to test and execute the backend logic—**it is not a reflection of frontend engineering or UI/UX design standards.**

---

## Tech Stack & Architecture

| Component | Technology | Purpose |
| :--- | :--- | :--- |
| **Core Framework** | FastAPI (Python) | High-performance asynchronous routing & Form processing |
| **AI LLM Engine** | Groq Cloud SDK (`llama-3.3-70b-versatile`) | Deep reasoning for instant contextual chat answers |
| **Database Mimic** | Local File System (`data.json`) | Structural practice of JSON file manipulation & error catching |
| **Session Control** | HTTP Cookies (`user_session`) | Core authentication state persistence across pages |
| **Frontend Bridge** | JavaScript (Vanilla Fetch API) | Handling background asynchronous POST payloads |

---

## Project Tree Structure

```text
├── api.py                 # Core FastAPI engine & route definitions
├── main.py                # External microservice script containing 'analyse_email'
├── data.json              # Persistent, file-based target for credential matrices
├── .env                   # Local system variables housing secret API keys
└── templates/             # Server-rendered HTML functional layouts
    ├── index.html         # Main workspace UI hosting the async chat box interface
    ├── login.html         # Login security frame
    └── signup.html        # Onboarding framework with strict input parsing

```

---

## Cloning the Repository

To get a local copy of this backend playground up and running on your machine, execute the following commands in your terminal:

```bash
# Clone the repository from GitHub
git clone https://github.com/vanig245/Smart-Email-Intelligence.git
```

## Installation & Deployment Guide

## 1. Replicate the Dependencies

Run the following installation command inside your virtual environment to install all required Python packages:

```bash
pip install fastapi uvicorn groq jinja2 python-multipart python-dotenv requests
```

---

## 2. Structure Local Environment Variables

Create a file named `.env` in the root directory (same folder as `api.py`) and add the following:

```env
GROQ_API_key="your_secret_groq_cloud_api_token_here"
```

---

## 3. Setup Local Storage Matrices

Create a file named `data.json` and initialize it with an empty JSON object:

```json
{}
```

---

## 4. Ignite the Uvicorn Application Server

Start the FastAPI ASGI server with hot-reload enabled:

```bash
uvicorn api:app --reload
```

---

## 5. Launch the Application

After the server starts successfully, open your browser and navigate to:

```text
http://127.0.0.1:8000/signuppage
```

You can now test and run transactional requests across the backend.