from fastapi import FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI(
    title="StoreAPI"
)
