FROM python:3.6-slim-stretch as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        python-dev \
        libpcre3 \
        libpcre3-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install \
    urllib3==1.22 \
    grequests==0.3.0 \
    flask==1.0.2

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt && rm -rf /root/.cache

COPY . /app
WORKDIR /app

CMD python3 run.py
