FROM python:3.10-alpine

RUN apk update \
    apk add \
    build-base \
    postgresql \
    postgresql-dev \
    libpq

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python","/code/app/app.py"]
