import fakeredis.aioredis
import pytest
from fastapi.testclient import TestClient

import app.redis_client as redis_client_module
from app.main import app


@pytest.fixture(scope="session")
def client():
    return TestClient(app)


@pytest.fixture(autouse=True, scope="function")
def mock_redis():
    fake_redis = fakeredis.aioredis.FakeRedis()
    redis_client_module.redis_client = fake_redis
    return fake_redis
