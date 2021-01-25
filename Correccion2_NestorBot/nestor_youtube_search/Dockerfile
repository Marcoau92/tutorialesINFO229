FROM python:3.6.3

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

ENV PYTHONUNBUFFERED=1

WORKDIR /nestor_youtube_search

COPY ./nestor_youtube_search.py /nestor_youtube_search.py

CMD [ "python", "/nestor_youtube_search.py" ]
