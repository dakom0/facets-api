# Facets API

> Facets Overview and Dive visualization built using a HTML page and Fast API

![Alt text](/relative/Screen Shot 2021-08-10 at 9.42.04 AM.png "Optional Title")

## Facets Overview
Overview gives a high-level view of one or more data sets. It produces a visual feature-by-feature statistical analysis, and can also be used to compare statistics across two or more data sets. 

## Facets Dive
Dive is a tool for interactively exploring up to tens of thousands of multidimensional data points, allowing users to seamlessly switch between a high-level overview and low-level details.

## Features

- Automatic data model documentation with JSON Schema (as OpenAPI itself is based on JSON Schema).
- Designed around these standards, after a meticulous study. Instead of an afterthought layer on top.
- Interactive API documentation with Swagger UI, with interactive exploration, call and test your API directly from the browser.


## Usage


### Install Dependencies (frontend & backend)

```
pip install facets-overview

pip install fastapi

pip install uvicorn[standard]
```

## Run

```
# Run frontend (:8000) 
open the html file on your browser

# Run backend (:5001)
uvicorn main:app --reload
```

## Endpoints (Swagger UI)
```
# Run backend (:5001)

uvicorn main:app --reload

Go to http://127.0.0.1:5001/docs
```
