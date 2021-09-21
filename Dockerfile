FROM python:3.9
ENV BARCODE 0
ENV PIN 0
ENV SESSION_CODE 0
ENV REQUEST_TIME 0
ENV TZ=America/Toronto
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip3 install --upgrade pip setuptools wheel
RUN pip3 install pandas
RUN pip3 install bs4
RUN pip3 install requests
RUN pip3 install lxml
RUN pip3 install numpy
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]