from setuptools import setup

setup(
    name="app",
    version="1.0",
    description="A useful store",
    author="Man Foo",
    author_email="eloy.colell@gmail.com",
    packages=["app"],  # same as name
    install_requires=[
        "wheel",
        "bar",
        "greek",
        "fastapi",
    ],  # external packages as dependencies
)
