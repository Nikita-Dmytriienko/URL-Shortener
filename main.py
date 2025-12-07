from contextlib import asynccontextmanager

from fastapi import FastAPI, Body

from database.db import engine
from database.models import Base

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all) #there is no logic for parallelizing migrations(from #docs), too rare
    yield
    
#lifespan
app = FastAPI(lifespan=lifespan)


#generate short url
@app.post("/short_url")
async def generate_short_url(
    long_url: str = Body(embeded=True)
):
    return {"data": 1}

@app.get("/{slug}")
async def redirect_to_url(slug: str):
    return ... #redirect