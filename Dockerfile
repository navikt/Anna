FROM navikt/python:3.8

USER root

COPY . .

RUN pip3 install -r requirements.txt

RUN python3 -m spacy download sv_core_news_sm

CMD ["python3", "main.py"]