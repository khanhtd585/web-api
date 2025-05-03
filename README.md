# FastAPI Webhook Receiver

A lightweight and secure Webhook receiver built with **FastAPI**. This project includes:

- ✅ API key-based security
- 📊 Prometheus-compatible metrics
- 📈 Request logging
- ⚡ High performance (async, Uvicorn)

---

## 📁 Project Structure

webhook_app/
├── main.py # Entry point for FastAPI application
├── config.py # Configuration loader (.env support)
├── logger.py # Logging setup
├── requirements.txt # Python dependencies
└── .env # Environment variables (e.g., API key)

## Run the application
uvicorn main:app --reload
