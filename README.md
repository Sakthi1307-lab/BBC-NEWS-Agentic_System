# BBC News Agentic System

A LangGraph agent that routes questions between a local BBC News index and live web search, grades retrieved documents, and generates an answer with Groq.

## Setup

1. Create and activate a Python virtual environment.
2. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and set `GROQ_API_KEY` and `TAVILY_API_KEY`.
4. Build the local BBC index:

   ```powershell
   $env:PYTHONPATH = "."
   python scripts\build_index.py
   ```

5. Run the application:

   ```powershell
   python main.py
   ```

The `.env` file and virtual environment are intentionally excluded from Git.
