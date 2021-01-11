FROM python:3.6.3

ENV SLACK_TOKEN="xoxb-77335436279-1431847376817-ImrCYcY3SRXQhIKwJ4Dvuuyl"
ENV SLACK_SIGNING_SECRET="929e1515059e1a1a2f2162d4a059df78"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_slack_reader_2

COPY ./nestor_slack_reader_2.py /nestor_slack_reader_2.py

CMD [ "python", "/nestor_slack_reader_2.py" ]
