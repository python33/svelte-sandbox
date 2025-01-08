FROM python:3.11-alpine

WORKDIR /app

RUN  apk add --no-cache postgresql-libs && \
	apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev zlib-dev jpeg-dev linux-headers libffi-dev rust cargo && \
	apk add --no-cache python3 python3-dev &&\
        rm -rf /var/cache/apk/* &&\
        python3 -m ensurepip

COPY ./requirements.txt /etc/requirements.txt

RUN python3 -m pip install --upgrade pip && \
	CRYPTOGRAPHY_DONT_BUILD_RUST=1 python3.11 -m pip install --no-cache-dir -r /etc/requirements.txt

RUN python3 -m pip install gunicorn

CMD gunicorn knowledge_base.wsgi -b 0.0.0.0:8000
