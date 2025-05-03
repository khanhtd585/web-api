from fastapi import FastAPI, Request, Header, HTTPException, status, Depends
from prometheus_fastapi_instrumentator import Instrumentator
from logger import logger
from config import API_KEY

app = FastAPI()

# Metrics instrumentation
Instrumentator().instrument(app).expose(app)

# Middleware to log requests/responses
@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Incoming request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

# Security dependency
def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        logger.warning("Unauthorized access attempt.")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API Key"
        )

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/webhook", dependencies=[Depends(verify_api_key)])
async def webhook_handler(request: Request):
    body = await request.json()
    logger.info(f"Webhook payload: {body}")
    # Do processing here...
    return {"status": "received", "data": body}
