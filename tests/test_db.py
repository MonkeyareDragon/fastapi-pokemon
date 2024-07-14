import pytest
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import SessionLocal

@pytest.mark.asyncio
async def test_db_connection():
    async with SessionLocal() as session:
        assert isinstance(session, AsyncSession)
