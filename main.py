from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
testNumber = 10


@app.get("/")
async def root():
    return {"number": testNumber}


class b(BaseModel):
    by: int


@app.post("/increment")
async def increment(b: b):
    global testNumber
    testNumber += int(b.by)
    return {"number": testNumber}


@app.post("/decrement")
async def decrement(b: b):
    global testNumber
    testNumber -= int(b.by)
    return {"number": testNumber}

