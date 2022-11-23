from typing import Generator

import pytest
from app.db import engine
from app.main import app
from fastapi.testclient import TestClient
from sqlmodel import Session


@pytest.fixture()
def client() -> Generator:
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def db() -> Session:
    with Session(engine) as session:
        yield session.exec
