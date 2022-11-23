FROM python:3.10-slim-buster AS backend_web

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install python dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
# add app
COPY . .
RUN pip install -r requirements.txt

FROM backend_web as backend_dev

# install system dependencies
RUN apt-get update \
  && apt-get -y install libpq-dev python3-dev curl git postgresql \
  && apt-get clean
RUN curl https://cli-assets.heroku.com/install.sh | sh

RUN pip install -r requirements_dev.txt
