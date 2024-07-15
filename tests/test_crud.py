import pytest
from app.db.database import SessionLocal
from app.utilis import create_pokemon

@pytest.mark.asyncio
async def test_create_pokemon():
    async with SessionLocal() as session:
        new_pokemon = await create_pokemon(session, name="Pikachu", image="image_url", type="Electric")
        assert new_pokemon.name == "Pikachu"
        assert new_pokemon.image == "image_url"
        assert new_pokemon.type == "Electric"
        