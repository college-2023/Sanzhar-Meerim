FROM python:3.8

ENV PYTHONUNBUFFERED 1

WORKDIR /home/ubuntu/Sanzhar-Meerim/actions-runner/_work/Sanzhar-Meerim/Sanzhar-Meerim

COPY . .

RUN python -m pip install --upgrade pip setuptools wheel

RUN pip install -r req.txt
