from contextlib import asynccontextmanager
from typing import Annotated, AsyncGenerator

from fastapi import Depends, FastAPI, Body, status, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import engine, new_session
from src.database.models import Base

from src.exceptions import NoLongUrlFoundError, SlugAlreadyExistError
from src.service import generate_short_url, get_url_by_slug

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all) #there is no logic for parallelizing migrations(from #docs), too rare
    yield
    
#lifespan
app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

async def get_session() -> AsyncGenerator[AsyncSession,None ]:
    async with new_session() as session:
        yield session


#generate short url
@app.post("/short_url")
async def generate_slug(
    session: Annotated[AsyncSession, Depends(get_session)], 
    long_url: Annotated[str, Body(embed=True)],
):
    try:
        new_slug = await generate_short_url(long_url, session)
    except SlugAlreadyExistError:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="Cant create this slug")
        
    return {"data": new_slug}

@app.get("/{slug}")
async def redirect_to_url( 
    slug: str,
    session: Annotated[AsyncSession, Depends(get_session)], 
):
    try:
        long_url = await get_url_by_slug(slug, session)
    except NoLongUrlFoundError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Link doesnt exist")
    return RedirectResponse(url=long_url,status_code=status.HTTP_302_FOUND) #redirect