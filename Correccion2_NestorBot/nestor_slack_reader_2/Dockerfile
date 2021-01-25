FROM python:3.6.3

#ENV SLACK_TOKEN="1632151781382.1636081307973"
ENV SLACK_TOKEN="odmsNhDR77ws5hPWy0fMSZvT"

ENV SLACK_SIGNING_SECRET="feda19d40090ee3e36b7559bbd710603"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]