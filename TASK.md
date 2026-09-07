## Application Process - Coding Task

### Introduction

The task is to write a little API. Nothing really complicated, no remote-accessible databases or anything.
You are provided with two pairs of files. One file is always the source file, the other one is the target file.
The data in the target file needs to somehow be transformed from the source file. How? You have to figure out.

The data of the source file then needs to be shared from the API. The API should have a way to filter the data by
multiple desired RICs (#RIC). For querying a single RIC, we would like to see a HTTP GET request, for querying multiple
RICs, we would like to see a HTTP POST request.

### Technical Requirements

- Python 3.14+
- Typer interface, configurable also via environment variables.
- Pydantic and CSV models for the target data (say, ?type=csv or ?type=json).
- FastAPI framework.
- No pandas allowed.
- Data tools that are allowed include:
    - pyarrow
    - DuckDB
    - chdb (serverless-clickhouse)
- Docker image for the API using the 12-factor app methodology.
- poetry or uv build tooling.

### Evaluation Criteria

- The API should be easy to use and have some swagger documentation.
- The API should be able to filter the data by one RIC (GET) and multiple RICs (POST).
- The API should be able to transform the data from the source file to the target file and json (in the format of the
  target file).
- You will be able to precisely explain the technical decisions you made and how it works exactly and in detail. This is
  important because we want to assess you, not your coding agents or LLM.
- Clean code (Hint: mypy, flake8 / ruff; good names and *complete* type hints!).
- At least one test for one of the endpoints (e.g. A query w/ ric-filter will yield the expected file)