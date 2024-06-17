import uvicorn
from fastapi import FastAPI
import pathlib
from typing import Optional
from build_model import build_model, get_vectorizer, make_prediction
from contextlib import asynccontextmanager
from cassandra.cqlengine.management import sync_table
from . import (config, models, db)

BASE_DIR = pathlib.Path(__file__).resolve().parent.parent
VECTORIZER_METADATA_PATH = BASE_DIR / "vectorizer_metadata.json"
MODEL_PATH = BASE_DIR / "model.keras"

model_dict = {}

@asynccontextmanager
async def lifespan(app : FastAPI):
    global MODEL_PATH
    global VECTORIZER_METADATA_PATH

    model = build_model(MODEL_PATH)
    vectorizer = get_vectorizer(VECTORIZER_METADATA_PATH)
    model_dict['model'] = model
    model_dict['vectorizer'] = vectorizer
    model_dict['db_session'] = db.get_session()
    model_dict['inference_model'] = models.SpamInference
    sync_table(model_dict['inference_model'])
    yield
    model_dict.clear()


app = FastAPI(lifespan = lifespan)
settings = config.get_settings()

@app.get('/predict')
def return_pred(q:Optional[str] = None):
    vectorizer = model_dict['vectorizer']
    model = model_dict['model']
    query = q or "Hello World"
    pred = make_prediction(query, vectorizer, model)
    data = {"query" : query,
            "label" : pred}
    inference_model = model_dict['inference_model']
    object = inference_model.objects.create(**data)
    return object

@app.get('/inferences')
def list_all():
    lst = model_dict['inference_model'].objects.all()
    return list(lst)






