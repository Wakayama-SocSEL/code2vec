FROM tensorflow/tensorflow:2.0.1-gpu-py3

RUN apt-get update && apt-get upgrade -y &&\
    apt-get install -y nodejs npm sudo

RUN pip install -U pip && \
    pip3 install -U pandas

RUN npm install -g n && \
    n stable && \
    apt-get purge -y nodejs npm

COPY . /code2vec
RUN cd /code2vec/JSExtractor/JSExtractor; npm install
