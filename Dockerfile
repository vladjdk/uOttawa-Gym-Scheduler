FROM python:3.9-buster

WORKDIR /usr/src/app
COPY . .

ENV REQUEST_TIME 0

RUN pip install scipy
RUN pip install pandas
RUN pip install numpy
RUN pip install setuptools
RUN pip install requests
RUN pip install beautifulsoup4
RUN pip install lxml
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]