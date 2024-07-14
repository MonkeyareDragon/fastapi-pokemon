import httpx
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.database import SessionLocal, engine
from app.db.init_db import init_db
from app.crud import create_pokemon

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize the database
    await init_db(engine)
    
    async with httpx.AsyncClient() as client:
        response = await client.get('https://pokeapi.co/api/v2/pokemon?limit=100')
        pokemons = response.json()['results']
        
        async with SessionLocal() as db:
            for pokemon in pokemons:
                pokemon_detail = await client.get(pokemon['url'])
                pokemon_data = pokemon_detail.json()
                await create_pokemon(db, name=pokemon_data['name'], 
                                     image=pokemon_data['sprites']['front_default'],
                                     type=pokemon_data['types'][0]['type']['name'])
    yield

app = FastAPI(lifespan=lifespan)

