FROM continuumio/miniconda3
RUN conda create -n env python=3.6
RUN echo "source activate env" > ~/.bashrc
ENV PATH /opt/conda/envs/env/bin:$PATH

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