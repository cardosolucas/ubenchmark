FROM python:3.7-buster

USER root

#########################################
#   Install here your OS dependencies   #
#########################################

#apt install <dependency>

RUN mkdir benchmark
RUN mkdir logs

ENV UBENCH_LOG=/root/logs

ADD benchmark benchmark/
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "/bin/bash", "-c", "cd benchmark && bash bench.sh" ] 