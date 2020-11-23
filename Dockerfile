FROM python:3.7-alpine

ARG VERSION

RUN pip install onepanel-sdk==$VERSION

CMD python