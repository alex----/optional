FROM python:3.5-slim
ADD . /optional
RUN cd /optional && pip3 install -e . && python3 -m unittest discover
FROM python:2.7-slim
ADD . /optional
RUN cd /optional && pip install -e . && python -m unittest discover