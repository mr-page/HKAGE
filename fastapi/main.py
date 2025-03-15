from fastapi import FastAPI,Query
from pydantic import  BaseModel
import uvicorn

app = FastAPI()

@app.get("/demo")
async def demo_get(
        a: int = Query(..., description="first integer"),
)