from database.models import Base
from main import app, get_session

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

import pytest


engine = create_async_engine(
    url="", 
    pool_size=20,
    max_overflow=30,
)

new_session = async_sessionmaker(bind=engine, expire_on_commit=False)



async def get_test_session() -> AsyncGenerator[AsyncSession,None]:
    async with new_session() as session:
        yield session
        

app.dependency_overrides[get_session] = get_test_session

@pytest.fixture(scope="session")
async def setup_db():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)
