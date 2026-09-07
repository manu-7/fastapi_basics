# FastAPI Basics
 
A beginner-to-intermediate FastAPI learning repo. Each folder covers a core concept with working code and tests. More added as I go.
 
## Topics Covered
 
- **asynchronous** – async/await patterns in FastAPI
- **CORS** – cross-origin resource sharing setup
- **CRUD** – basic Create, Read, Update, Delete endpoints
- **dependency** – dependency injection with `Depends`
- **file_Upload** – handling file uploads
- **JWT** – authentication using JSON Web Tokens
- **middleware** – custom middleware implementation
- **Response_Model** – Pydantic response models & validation
- **sqlalchemy** – database integration with SQLAlchemy ORM
- **testing** – API testing using `pytest` and `TestClient`
## Tech Stack
 
- Python
- FastAPI
- SQLAlchemy
- Pytest
- Uvicorn
## Running Locally
 
```bash
# clone the repo
git clone https://github.com/manu-7/fastapi_basics.git
cd fastapi_basics
 
# create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # macOS/Linux
 
# install dependencies
pip install -r requirements.txt
 
# run the app
uvicorn main:app --reload
```
 
## Running Tests
 
```bash
pytest
```
 
## Structure
 
Each concept lives in its own folder with:
- `main.py` — implementation
- `test_main.py` — tests for that concept
