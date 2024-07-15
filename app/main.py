import httpx
from fastapi import FastAPI, Depends, status
from fastapi_pagination import add_pagination, Page, paginate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from contextlib import asynccontextmanager
from app.db.database import SessionLocal, engine, get_db, Base
from app.db.init_db import init_db
from app.utilis import create_pokemon
import app.schemas as schemas
import app.models as models

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database
    await init_db(engine)
    
    async with httpx.AsyncClient() as client:
        # Check if the database is empty
        async with SessionLocal() as db:
            stmt = select(models.Pokemon)
            result = await db.execute(stmt)
            pokemons = result.scalars().all()
            
            if not pokemons:
                response = await client.get('https://pokeapi.co/api/v2/pokemon?limit=100')
                pokemons = response.json()['results']
                
                for pokemon in pokemons:
                    pokemon_detail = await client.get(pokemon['url'])
                    pokemon_data = pokemon_detail.json()
                    await create_pokemon(db, name=pokemon_data['name'], 
                                         image=pokemon_data['sprites']['front_default'],
                                         type=pokemon_data['types'][0]['type']['name'])
                await db.commit()
    yield

app = FastAPI(lifespan=lifespan)

@app.get("/api/v1/pokemons", response_model=Page[schemas.Pokemon])
async def read_pokemons(db: AsyncSession = Depends(get_db)):
    stmt = select(models.Pokemon)
    result = await db.execute(stmt)
    pokemons = result.scalars().all()
    return paginate(pokemons)

# Add pagination support to the FastAPI app
add_pagination(app)
