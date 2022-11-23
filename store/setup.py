from setuptools import setup

packages = ["app", "app.models", "app.routers.v1", "app.services"]

package_data = {"": ["*"]}

install_requires = [
    "alembic>=1.8.1,<2.0.0",
    "asyncpg>=0.27.0,<0.28.0",
    "fastapi>=0.87.0,<0.88.0",
    "sqlalchemy-utils>=0.38.3,<0.39.0",
    "sqlmodel>=0.0.8,<0.0.9",
    "uvicorn>=0.19.0,<0.20.0",
]

setup_kwargs = {
    "name": "app",
    "version": "0.1.0",
    "description": "",
    "long_description": "",
    "author": "eloy",
    "author_email": "eloy.colell@gmail.com",
    "maintainer": "None",
    "maintainer_email": "None",
    "url": "None",
    "packages": packages,
    "package_data": package_data,
    "install_requires": install_requires,
    "python_requires": ">=3.10,<4.0",
}


setup(**setup_kwargs)
