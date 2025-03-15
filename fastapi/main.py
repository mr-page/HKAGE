from typing import Optional

from fastapi import FastAPI

app = FastAPI() # 建立一個 Fast API application

@app.get("/12l/") # 指定 api 路徑 (get方法)
def read_root():
    print("sd")
    return {"Hello": "Worgsdgsgggdsdgdgld"}




@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}