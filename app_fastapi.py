from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS
origins = [
    "http://localhost:8080",  # Vue.js dev server
    "http://localhost:8000"   # FastAPI server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str

@app.post("/api/greet")
async def greet(item: Item):
    greeting = f"Hello, {item.name}!"
    return {"greeting": greeting}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)