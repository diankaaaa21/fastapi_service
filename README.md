# Phone Address Storage API

## Description
An asynchronous FastAPI service for storing addresses associated with phone numbers using Redis.

Implemented features:
- Create and update phone address records
- Retrieve address by phone number
- Healthcheck endpoint to monitor Redis connection
- Asynchronous request handling
- Docstrings and clean architecture
- Dockerized for quick setup and deployment

## Project Startup

```bash
git clone https://github.com/diankaaaa21/fastapi_service.git

cd fastapi_service

docker-compose up --build
```

## Running Tests
This project uses pytest for testing.

To run the tests locally:
```bash
cd fastapi_service

pip install -r requirements.txt

pytest -v
```