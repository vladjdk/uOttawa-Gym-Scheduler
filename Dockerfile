FROM python:3.7
ENV BARCODE 0
ENV PIN 0
ENV SESSION_CODE 0
ENV REQUEST_TIME 0
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir --default-timeout=100 pandas
RUN pip install --no-cache-dir --default-timeout=100 bs4
RUN pip install --no-cache-dir --default-timeout=100 requests
RUN pip install --no-cache-dir --default-timeout=100 lxml
RUN pip install --no-cache-dir --default-timeout=100 numpy
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]