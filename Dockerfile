FROM python:3.9-buster
COPY . .
ENV REQUEST_TIME 0

RUN pip install -r requirements.txt
RUN pip install --upgrade pip

ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["/opt/venv/bin/python","runner.py","$REQUEST_TIME"]