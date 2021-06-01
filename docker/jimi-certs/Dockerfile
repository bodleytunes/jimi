FROM python:3.9-slim as base

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1


RUN apt-get update && \
    apt-get install -y --no-install-recommends openssl  && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /home

COPY docker/jimi-certs/entrypoint.sh ./
RUN chmod 700 entrypoint.sh

WORKDIR /certs

#CMD ["/certs/gen_certs.sh"]
