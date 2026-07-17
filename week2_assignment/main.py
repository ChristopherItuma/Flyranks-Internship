from fastapi import FastAPI

app = FastAPI()

# Root endpoint that returns basic information about the API
@app.get("/")
async def read_root():
    return { "name": "Task API", "version": "1.0", "endpoints": ["/tasks"] }

# Health check endpoint that returns a simple message indicating the API is running
@app.get("/health")
async def health_check():
    return { "status": "ok" }