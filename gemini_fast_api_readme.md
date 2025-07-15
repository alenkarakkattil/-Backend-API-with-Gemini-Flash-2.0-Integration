# Gemini FastAPI Backend

This project is a lightweight backend application built using **FastAPI** that connects to **Google's Gemini 2.0 Flash** model. It allows users to send text prompts and receive AI-generated responses via a simple RESTful API.

GitHub Repository: [https://github.com/alenkarakkattil/-Backend-API-with-Gemini-Flash-2.0-Integration](https://github.com/alenkarakkattil/-Backend-API-with-Gemini-Flash-2.0-Integration)

---

## Objective

To create a backend interface for interacting with Gemini's generative model using Python, showcasing:

* Proper API structure and endpoint design
* Integration with Google Generative AI (Gemini)
* Logging of response times and results

---

## Project Structure

```
project/
├── main.py                  # FastAPI app with endpoints
├── gemini_integration.py   # Gemini API integration logic
├── client.py               # Terminal-based test client
├── .env                    # Stores GEMINI_API_KEY
├── .env.example            # Template for environment variables
├── requirements.txt        # Required Python packages
├── README.md               # Project documentation
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/alenkarakkattil/-Backend-API-with-Gemini-Flash-2.0-Integration.git
cd -Backend-API-with-Gemini-Flash-2.0-Integration
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here (Replace `your_api_key_here` with your actual Gemini API key.)
```

You can get your API key from: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)

### 5. Run the FastAPI Server
```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to test the API in Swagger UI.

### 6. Run the Client(to run on terminal)
```bash
python client.py
```


## API Endpoints

### `GET /`
#### Returns: `{"message": "Gemini FastAPI Backend is running!"}`


### `POST /generate/`
#### Input JSON:
```json
{
  "prompt": "What is Artificial Intelligence?"
}
```
#### Output JSON:
```json
{
  "response": "Artificial Intelligence (AI) is..."
}
```


## Evaluation Criteria

### 1. API Structure and Endpoint Design
* FastAPI framework with clear route definitions
* Request validation using Pydantic models
* Separation of concerns with modular code

### 2. Gemini Integration Quality
* Integrated using `google.generativeai` SDK
* API key managed securely with `.env`
* Retry mechanism using `tenacity`
* Uses the `models/gemini-2.0-flash` model

### 3. Response Time and Reliability
* Response time logged using Python’s `time` module
* Automatic retry logic for improved reliability
* Console logs for all interactions

### 4. Logs and Outputs
Example log output in terminal:
```
Prompt: What is AI?
Response Time: 1.45s
Gemini Response: Artificial Intelligence (AI) is...
--------------------------------------------------
```

### 5. Basic Evaluation Method
* Manual testing via Swagger UI and `client.py`
* Console logs show real-time prompt/response tracking
* Retry logic demonstrates stability under failure conditions



## Demo Video
[Watch the demo on YouTube](https://youtube.com/your-demo-link)
