FROM python

WORKDIR /course/

COPY requirements.txt /course/

RUN pip install -r requirements.txt