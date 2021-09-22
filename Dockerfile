FROM python:3.7-buster
WORKDIR /usr/src/app
COPY . .

ENV REQUEST_TIME 0

RUN apt-get update --fix-missing && \
    apt-get -y upgrade && \
    apt-get install -y
RUN pip3 --default-timeout=1200 install scipy
RUN pip3 --default-timeout=1200 install pandas
RUN pip3 --default-timeout=1200 install numpy
RUN pip3 --default-timeout=1200 install setuptools
RUN pip3 --default-timeout=1200 install requests
RUN pip3 --default-timeout=1200 install beautifulsoup4
RUN pip3 --default-timeout=1200 install lxml
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]