from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Pokemon

async def create_pokemon(db: AsyncSession, name: str, image: str, type: str):
    db_pokemon = Pokemon(name=name, image=image, type=type)
    db.add(db_pokemon)
    await db.commit()
    await db.refresh(db_pokemon)
    return db_pokemon