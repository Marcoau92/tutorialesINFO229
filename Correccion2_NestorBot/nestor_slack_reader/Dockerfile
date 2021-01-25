FROM python:3.6.3

#ENV SLACK_TOKEN="1632151781382.1636081307973"
ENV SLACK_TOKEN="xoxb-1632151781382-1642373470919-TwpF6D5Fu2eqkYZQcqt5h7xC"

ENV SLACK_EVENTS_TOKEN="a898af63c2ef244ff2aa6a524ceb5d7d"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader

COPY ./nestor_slack_reader.py /nestor_slack_reader.py

CMD [ "python", "/nestor_slack_reader.py" ]