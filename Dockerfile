FROM python:3.7
ENV BARCODE=none
ENV PIN=none
ENV SESSION_CODE=none
ENV REQUEST_TIME=none
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy
RUN pip install pandas
RUN pip install bs4
RUN pip install requests
WORKDIR /usr/src/sched
COPY . .
CMD ["python3 runner.py $BARCODE $PIN $SESSION_CODE $REQUEST_TIME"]