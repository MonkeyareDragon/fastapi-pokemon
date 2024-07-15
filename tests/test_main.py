import pytest
from fastapi.testclient import TestClient
from httpx import AsyncClient
import asyncio
from app.main import app

client = TestClient(app)

@pytest.mark.asyncio
async def test_read_pokemons():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/pokemons")
    assert response.status_code == 200
    assert "items" in response.json()
    assert response.json()["items"] is not None

@pytest.mark.asyncio
async def test_read_pokemons_name():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/pokemons?name=pi")
    assert response.status_code == 200
    assert "items" in response.json()
    pokemons = response.json()["items"]
    assert pokemons is not None
    for pokemon in pokemons:
        assert "pi" in pokemon["name"].lower()

@pytest.mark.asyncio
async def test_read_pokemons_type():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/pokemons?type=electric")
    assert response.status_code == 200
    assert "items" in response.json()
    pokemons = response.json()["items"]
    assert pokemons is not None
    for pokemon in pokemons:
        assert pokemon["type"] == "electric"

@pytest.mark.asyncio
async def test_read_pokemons_name_and_type():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/api/v1/pokemons?name=pi&type=electric")
    assert response.status_code == 200
    assert "items" in response.json()
    pokemons = response.json()["items"]
    assert pokemons is not None
    for pokemon in pokemons:
        assert "pi" in pokemon["name"].lower()
        assert pokemon["type"] == "electric"

# Ensure the event loop used by pytest and AsyncClient is compatible
@pytest.fixture(scope="module")
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()