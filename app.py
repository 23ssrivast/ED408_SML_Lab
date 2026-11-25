from fastapi import FastAPI
from joblib import load
from pydantic import BaseModel

app = FastAPI()
model = load("digit_model.joblib")


class Trace(BaseModel):
    coordinates: list[int]


@app.post("/predict")
def predict(trace: Trace):
    x = [v / 100 for v in trace.coordinates]
    digit = model.predict([x])[0]
    return {"digit": int(digit)}
