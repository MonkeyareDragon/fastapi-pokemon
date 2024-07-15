import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_read_pokemons():
    response = client.get("/api/v1/pokemons")
    assert response.status_code == 200