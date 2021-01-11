FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-77335436279-1431847376817-ImrCYcY3SRXQhIKwJ4Dvuuyl"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
