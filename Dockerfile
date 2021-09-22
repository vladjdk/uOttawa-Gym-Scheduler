FROM python:3.7-slim
WORKDIR /usr/src/app
COPY . .

ENV REQUEST_TIME 0

RUN apt-get update  --fix-missing && \
    apt-get install -y \
        build-essential \
        make \
        gcc \
    && pip install -r requirements.txt \
    && apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]