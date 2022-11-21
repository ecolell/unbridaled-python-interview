import asyncio
from typing import Generator

import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.db import engine
from sqlmodel import Session


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def db() -> Session:
    with Session(engine) as session:
        yield session.exec
