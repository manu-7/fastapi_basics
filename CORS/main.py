from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware

app  = FastAPI()

#Allowed Origin(front-end URL)

origins= [
    "http://localhost:5173/"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins ,#allowed frontend
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers= ["*"]
)

@app.get("/")
def home():
    return{
        "message":"CORS enable API"
    }