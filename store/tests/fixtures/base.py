from typing import Generator

import pytest
from app.db import settings
from app.main import app
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlmodel import SQLModel


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def db():
    engine = create_engine(settings.async_database_url.replace("+asyncpg", ""))
    with engine.begin():
        SQLModel.metadata.drop_all(engine)
        SQLModel.metadata.create_all(engine)
        yield scoped_session(sessionmaker(bind=engine))
