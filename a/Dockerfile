FROM python:3.9

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y python3 python3-pip && \
    pip install redis



WORKDIR /app
COPY . .

RUN pip3 install redis

CMD python main.py