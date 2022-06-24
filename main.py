from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
testNumber = 10

origins = [
    '*'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    print(testNumber)
    return {"number": testNumber}


@app.get("/init")
async def initApp():
    return {"init": True}


class Body(BaseModel):
    by: int


@app.post("/increment")
async def increment(b: Body):
    global testNumber
    testNumber += int(b.by)
    return {"number": testNumber}


@app.post("/decrement")
async def decrement(b: Body):
    global testNumber
    testNumber -= int(b.by)
    return {"number": testNumber}

