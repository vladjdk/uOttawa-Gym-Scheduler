RUN pip3 install numpy
RUN pip3 install pandas
RUN pip3 install bs4
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","barcode","pin","session_code","request_time"]