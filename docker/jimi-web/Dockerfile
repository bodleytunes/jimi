FROM python:3.9-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /home/jimi

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.6

RUN apt-get update && \
    apt-get install -y --no-install-recommends git unzip wget ca-certificates build-essential && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install "poetry==$POETRY_VERSION"

COPY docker/jimi-web/pyproject.toml docker/jimi-web/poetry.lock ./

# Install venv in workdir via poetry 
RUN poetry config virtualenvs.in-project true && poetry install

# directory works
RUN mkdir data && mkdir data/log && mkdir plugins
WORKDIR /home/jimi/data

RUN wget https://raw.githubusercontent.com/z1pti3/jimi-docker/master/data/settings.json

RUN openssl genrsa -out private.pem 2048 && \ 
    openssl rsa -in private.pem -outform PEM -pubout -out sessionPub.pem \
    && openssl rsa -in private.pem -out sessionPriv.pem -outform PEM && \
    rm private.pem && \
    openssl req -newkey rsa:2048 -nodes -keyout web.key -x509 -days 365 -out web.cert -subj "/C=GB/ST=London/L=London/O=jimi/OU=jimi/CN=jimiproject"



FROM base as final

COPY --from=builder /home/jimi /home/jimi

# copy repo source code into container image
COPY core /home/jimi/core
COPY system /home/jimi/system
COPY web /home/jimi/web
COPY react-web /home/jimi/react-web

WORKDIR /home/jimi

COPY jimi_web.py jimi.py  ./

RUN head jimi_web.py -n -4 > jimi_web2.py && \
    rm jimi_web.py && \
    mv jimi_web2.py jimi_web.py

#RUN echo "from jimi_web import api\n\napplication = api.webServer\n\nif __name__ == '__main__':\n\tapplication.run()" > start.py
#RUN echo "gunicorn --bind 0.0.0.0:4443 --workers 4 --threads 10 --certfile=data/web.cert --key=data/web.key start" > start_web.sh

COPY docker/jimi-web/start_web.sh docker/jimi-web/start.py  ./
RUN chmod 700 start_web.sh

ENV PATH="/home/jimi/.venv/bin:$PATH"


