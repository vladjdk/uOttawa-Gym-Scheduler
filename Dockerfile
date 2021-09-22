FROM python:3.7-buster

RUN curl "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-armv7l.sh" -o "Miniconda.sh"
RUN bash ./Miniconda.sh
RUN conda config --add channels rpi
RUN conda update conda

WORKDIR /usr/src/app
COPY . .

ENV REQUEST_TIME 0

RUN conda install scipy
RUN conda install pandas
RUN conda install numpy
RUN conda install setuptools
RUN conda install requests
RUN conda install beautifulsoup4
RUN conda install lxml
ENV TZ=America/Detroit
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
WORKDIR /usr/src/sched
COPY . .
CMD ["python3","runner.py","$REQUEST_TIME"]