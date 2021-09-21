FROM python:3.7-slim
RUN apt-get update && apt-get -y dist-upgrade
RUN apt-get -y install python3-numpy
RUN apt-get -y install python3-pandas
ENV BARCODE 0
ENV PIN 0
ENV SESSION_CODE 0
ENV REQUEST_TIME 0
RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install lxml
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]