from fastapi import FastAPI,Depends,Header,HTTPException


app = FastAPI() 

#2nd
def verify_token(token: str = Header(None)):
    if token != "mysecrettoken":
        raise HTTPException(
            status_code=401,
            detail="unauthorized"
        )
    return {
        "user":"Authorized User"
    }
    
@app.get("/secure-user")
def secure_data(user = Depends(verify_token)):
    return {
        "message":"Secure data accessed",
        "user":user
    }



#1st
def common_logic():
    return {
        "message":"common logic executed"
    }
    
@app.get("/home")
def home(data = Depends(common_logic)):
    return data
