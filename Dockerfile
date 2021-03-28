FROM python:3.7
ENV BARCODE 0
ENV PIN 0
ENV SESSION_CODE 0
ENV REQUEST_TIME 0
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy
RUN pip install pandas
RUN pip install bs4
RUN pip install requests
RUN pip install lxml
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$BARCODE","$PIN","$SESSION_CODE","$REQUEST_TIME"]