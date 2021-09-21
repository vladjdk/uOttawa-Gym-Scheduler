FROM python:3.7-slim

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