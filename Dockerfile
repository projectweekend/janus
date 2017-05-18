FROM python:3
RUN pip install -U pytest
COPY . /src
RUN cd /src && pip install .
WORKDIR /src
