# FastAPI app for model inference
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    title: str
    description: str
    price: float

@app.get("/")
def read_root():
    return {"message": "E-commerce Success Prediction API"}

@app.post("/predict")
def predict(item: Item):
    # Dummy prediction for now
    return {"success_probability": 0.5}
