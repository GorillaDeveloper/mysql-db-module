FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y python3 python3-pip

WORKDIR /usr/app/src

COPY mysqlcode /usr/app/src/mysqlcode
COPY requirements.txt ./

RUN pip3 install -r requirements.txt

CMD ["python3", "/usr/app/src/mysqlcode/main.py"]
