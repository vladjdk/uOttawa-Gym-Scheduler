FROM python:3.7-buster
WORKDIR /usr/src/app
COPY . .

ENV REQUEST_TIME 0

RUN apt-get update --fix-missing && \
    apt-get -y upgrade && \
    apt-get install -y
RUN apt-get install -y python3-pandas
RUN apt-get install -y python3-numpy
RUN pip install -r requirements.txt

ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]