FROM python:3.8-slim-buster
RUN sudo apt-get install python3-numpy
RUN pip3 install pandas
RUN pip3 install bs4
RUN pip3 install requests
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","barcode","pin","session_code","request_time"]