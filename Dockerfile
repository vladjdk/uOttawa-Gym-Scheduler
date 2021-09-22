FROM python:3.9-buster
COPY . .
ENV REQUEST_TIME 0

RUN python3 -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install -r requirements.txt

ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["/opt/venv/bin/python","runner.py","$REQUEST_TIME"]