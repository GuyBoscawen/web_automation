FROM ubuntu:18.04
RUN apt-get update

SHELL ["/bin/bash", "-c"]

RUN apt-get install -y -q build-essential
RUN apt-get install -y python3.8 python3-pip wget
RUN apt-get install -y python3.8-dev
RUN apt-get install -y python3.8-venv

RUN mkdir tmp/img_logs
RUN mkdir tmp/html_logs
RUN mkdir deployment
COPY requirements.txt /deployment/requirements.txt
COPY app /deployment/
RUN python3.8 -m venv /deployment/nate_env
RUN source /deployment/nate_env/bin/activate
RUN /deployment/nate_env/bin/pip install wheel
RUN /deployment/nate_env/bin/pip install -r /deployment/requirements.txt

WORKDIR /deployment/

ENV PYTHONUNBUFFERED=1
CMD ./nate_env/bin/python web_automation.py -d chrome
