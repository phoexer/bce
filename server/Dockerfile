FROM python:3.6

ENV        PYTHONUNBUFFERED 1

RUN        mkdir /var/app
WORKDIR    /var/app

COPY       manage.py /var/app/
COPY       requirements.txt /var/app/requirements.txt
RUN        pip install -r /var/app/requirements.txt --no-cache-dir

COPY       . /var/app/

EXPOSE     8000
