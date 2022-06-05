FROM python:3.9-slim-buster

RUN apt update && apt upgrade -y
RUN apt install git -y
COPY requirements.txt /requirements.txt

RUN cd /
RUN pip3 install -U pip && pip3 install -U -r requirements.txt
RUN mkdir /Doctor_Strange-BOT
WORKDIR /Doctor_Strange-BOT
COPY strange.sh /strange.sh
CMD ["/bin/bash", "/strange.sh"]
