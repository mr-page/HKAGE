# from fastapi import FastAPI,Query
# from pydantic import  BaseModel
# import uvicorn
#
# app = FastAPI()
#




from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated

app = FastAPI()
security = HTTPBasic()

# Mock user database (in a real app, use a proper database with hashed passwords)
fake_users_db = {
    "user1": {
        "username": "user1",
        "password": "password1",
        "full_name": "User One",
        "role": "admin"
    },
    "user2": {
        "username": "user2",
        "password": "password2",
        "full_name": "User Two",
        "role": "user"
    }
}


def authenticate_user(username: str, password: str):
    user = fake_users_db.get(username)
    if not user or user["password"] != password:
        return False
    return user


# @app.get("/")
# async def root():
#     return {"message": "Welcome to the authentication API"}


@app.get("/protected")
async def protected_route(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    return {
        "message": f"Hello {user['full_name']}!",
        "user_details": {
            "username": user["username"],
            "role": user["role"]
        }
    }


@app.get("/greet")
async def greet_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    user = authenticate_user(credentials.username, credentials.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    if user["role"] == "admin":
        return {"message": f"Welcome back, Administrator {user['full_name']}!"}
    else:
        return {"message": f"Hello {user['full_name']}, nice to see you again!"}
