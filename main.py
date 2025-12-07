from contextlib import asynccontextmanager

from fastapi import FastAPI, Body, status
from fastapi.responses import RedirectResponse

from database.db import engine
from database.models import Base

from service import generate_short_url

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all) #there is no logic for parallelizing migrations(from #docs), too rare
    yield
    
#lifespan
app = FastAPI(lifespan=lifespan)


#generate short url
@app.post("/short_url")
async def generate_slug(
    long_url: str = Body(embeded=True)
):
    new_slug = await generate_short_url(long_url)
    return {"data": new_slug}

@app.get("/{slug}")
async def redirect_to_url(slug: str): 
    return RedirectResponse(url=...,status_code=status.HTTP_302_FOUND) #redirect