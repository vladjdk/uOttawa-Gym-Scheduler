FROM python:3.7-stretch

WORKDIR /usr/src/app COPY . .

RUN apt-get update \
    && apt-get install build-essential make gcc -y \
    && apt-get install dpkg-dev -y \
    && apt-get install libjpeg-dev -y \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get auto-remove -y \
    && rm -rf /var/lib/apt/lists/* \
    && find /usr/local/lib/python3.7 -name "*.pyc" -type f -delete

RUN pip install --upgrade pip setuptools wheel
RUN pip3 install numpy
RUN pip3 install pandas
ENV REQUEST_TIME 0
RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install lxml
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]