FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-1632151781382-1642373470919-TwpF6D5Fu2eqkYZQcqt5h7xC"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /nestor_slack_writer

COPY ./nestor_slack_writer.py /nestor_slack_writer.py
COPY ./nestor_slack_writer.py /nestor_slack_writer.py

CMD [ "python", "/nestor_slack_writer.py" ]
