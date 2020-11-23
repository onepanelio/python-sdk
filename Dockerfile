FROM python:3.7-alpine

RUN pip install onepanel-sdk==$VERSION

CMD python