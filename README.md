# Task 1: Streamlit Interface for Local LLM (Ollama)

## Overview
This project implements a simple and interactive Streamlit web interface connected to a locally installed Large Language Model (LLM) using Ollama.

The application allows users to input queries and receive real-time responses from the locally running LLM.


## Technologies Used
- Python
- Streamlit
- Ollama
- Local LLM (TinyLlama / Llama 3 via Ollama)


## Features Implemented
- Text input box for user queries
- Model-generated response display
- Conversation history panel
- Reset/Clear chat button
- Smooth communication between Streamlit frontend and Ollama backend

## How It Works
1. The user enters a query in the Streamlit interface.
2. The query is sent to the locally running LLM via Ollama.
3. The model generates a response.
4. The response is displayed in the app along with conversation history.


## How to Run

### 1. Install Requirements
```bash
pip install -r requirements.txt
```

### 2. Make Sure Ollama is Installed and Running
```bash
ollama run tinyllama
```

### 3. Run Streamlit App
```bash
streamlit run app.py
```


## Learning Outcome
- Understood local LLM deployment
- Integrated frontend with backend LLM API
- Built interactive AI-based web interface
