FROM python:3
LABEL authors='Pvl1307'

WORKDIR /code

COPY pyproject.toml .

RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev --no-root

COPY . .