FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/actions-runner/_work/Online-Recording-System/Online-Recording-System

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip3 install -r req.txt
