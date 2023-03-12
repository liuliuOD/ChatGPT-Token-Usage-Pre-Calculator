FROM python:3

WORKDIR /app

COPY main.py pyproject.toml poetry.lock .

RUN pip install poetry

RUN poetry install

ENTRYPOINT ["poetry", "run", "python"]
CMD ["main.py"]
