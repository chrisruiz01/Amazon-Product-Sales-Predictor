# from curses import meta
from fastapi import FastAPI
from typing import Optional, List

from pydantic import BaseModel, Field, constr           # added Field, constr
from common.model import get_predictions
import numpy as np

app = FastAPI()

class Item(BaseModel):
    # review: List[str]
    review: List[constr(min_length=3, max_length=500)]  # added validation

@app.post("/predict_probability")                       # endpoint
def predict_probability(item: Item):
    # document = item.review
    document = (item.review)                            # item.review is already a list of strings
    # result = {}
    result = get_predictions(document)                  # Directly assign the predictions to result
    return result