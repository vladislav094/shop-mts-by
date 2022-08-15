FROM python:3.9.7-buster

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.13

# Install poetry.
RUN pip install "poetry==$POETRY_VERSION"

# Copy the poetry files to speed up builds.
WORKDIR /code
COPY poetry.lock pyproject.toml ./

# Install dependencies via Poetry.
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

# Copy the source code into the image.
RUN mkdir allure-reports
COPY framework ./framework
COPY tests ./tests
COPY jenkinsfiles ./jenkinsfiles
COPY pytest.ini ./