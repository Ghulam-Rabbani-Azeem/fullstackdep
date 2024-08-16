from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS (Cross-Origin Resource Sharing) for local development
origins = [
    "http://127.0.0.1:8000",
    "http://localhost:8000",
    "http://127.0.0.1:5500", # Add your port if you use a different one for serving the HTML
    "http://localhost:5500"  # This is an example port; change according to your setup
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/data")
def read_data():
    return {"message": "Hello from the FastAPI backend!"}
