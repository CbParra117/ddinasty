FROM python:3.9-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /src

WORKDIR /src

COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps \
    build-base \
    libffi-dev \
    linux-headers \
    ca-certificates \
    gcc \
    mariadb-dev \
    musl-dev \
    jpeg-dev \
    zlib-dev \
    glib \
    && python -m pip install -r requirements.txt \
    && find /usr/local \
    \( -type d -a -name test -o -name tests \) \
    -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
    -exec rm -rf '{}' + \
    && runDeps="$( \
        scanelf --needed --nobanner --recursive /usr/local \
                | awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \
                | sort -u \
                | xargs -r apk info --installed \
                | sort -u \
    )" \
    && apk add --virtual .rundeps $runDeps \
    && apk del .build-deps

ADD . .