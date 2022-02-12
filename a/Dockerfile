FROM python:3.9

RUN apt-get update
RUN apt-get -y upgrade

WORKDIR /app
COPY . .

CMD python main.py