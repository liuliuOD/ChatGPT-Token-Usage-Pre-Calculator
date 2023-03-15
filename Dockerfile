FROM python:3

WORKDIR /app

COPY *.py pyproject.toml poetry.lock .
COPY config config

RUN pip install poetry

RUN poetry install

ENTRYPOINT ["poetry", "run", "python"]
CMD ["main.py"]
