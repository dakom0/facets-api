import core

from typing import Optional

from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

# Load UCI census train and test data into dataframes.

from facets_overview.generic_feature_statistics_generator import GenericFeatureStatisticsGenerator

# Create the feature stats for the datasets and stringify it.
# Display the facets overview visualization for this data

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://127.0.0.1:8000/",
]

# Protostring for Faceets Overview
@app.get("/vaex_proto")
def read_data():
    return {"item": core.vaex_proto()}


@app.get("/vaex_data")
def read_data():
    return {"item": core.vaex_data() }


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="info")