FROM python:3.10-alpine

RUN apk update \
    apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt
COPY ./entrypoint.sh /

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
