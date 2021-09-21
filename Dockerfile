FROM python:3.8.5
ENV BARCODE 0
ENV PIN 0
ENV SESSION_CODE 0
ENV REQUEST_TIME 0
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir pandas
RUN pip install --no-cache-dir bs4
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir lxml
RUN pip install --no-cache-dir numpy
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]