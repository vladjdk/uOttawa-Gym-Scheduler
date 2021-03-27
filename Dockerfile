FROM python:3.7
RUN pip install --upgrade pip setuptools wheel
RUN pip install numpy
RUN pip install pandas
RUN pip install bs4
RUN pip install requests
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","barcode","pin","session_code","request_time"]