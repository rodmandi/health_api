FROM python:3.6-slim-stretch as builder

RUN apt-get update && apt-get install -y --no-install-recommends \
        git \
        build-essential \
        python-dev \
        libpcre3 \
        libpcre3-dev \
	&& rm -rf /var/lib/apt/lists/*

RUN pip3 install numpy==1.16
RUN pip3 install scipy==1.2.0
RUN pip3 install pandas==0.23.4

RUN pip3 install \
    urllib3==1.22 \
    pymongo==3.7.1 \
    dateparser==0.7.0 \
    daterangeparser==1.3.1 \
    python_dateutil==2.7.3 \
    protobuf==3.6.1 \
    google_api_python_client==1.7.4 \
    grequests==0.3.0 \
    isodate==0.6.0 \
    mysql_connector_python==8.0.5 \
    pyparsing==2.2.1 \
    pytz==2018.5 \
    flask==1.0.2

COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt && rm -rf /root/.cache

COPY . /app
WORKDIR /app

CMD python3 run.py
