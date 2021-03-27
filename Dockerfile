FROM gliderlabs/alpine
RUN apk add --no-cache --update \
    python3 python3-dev gcc \
    gfortran musl-dev
RUN pip3 install --upgrade pip setuptools && \
    pip3 install -r numpy

RUN pip install pandas
RUN pip install bs4
RUN pip install requests
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","barcode","pin","session_code","request_time"]