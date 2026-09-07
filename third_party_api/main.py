from fastapi import FastAPI
import requests

app = FastAPI()

# Get all data
@app.get("/posts")
def get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(response.status_code, response.text[:20])
    return response.json()