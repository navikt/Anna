import spacy
import numpy as np

nlp = spacy.load('sv_core_news_sm')
stoppord = ["hej", "nej"]


class Anna:
    def hej(self):
        # fråga = inmatning(input())
        # if "bot" in fråga:
        #     print("Jag är ingen bot! Jag är en väldigt, väldigt vacker tjej")
        # else:
        print(slumpmassigtSvar())


def inmatning(text: str):
    # todo rense teksten
    # todo vektorisere
    return rensare(text)


def rensare(text: str):
    rensade_text = text.lower()
    # todo fjerne andre tegn en ?
    text_utan_stoppord = [ord.replace("?", "") for ord in rensade_text.split(" ") if ord not in stoppord]
    return text_utan_stoppord


def slumpmassigtSvar():
    with open("boten_anna.txt", "r") as f:
        sangen = f.readlines()

    sang = [linje.replace("\n", "") for linje in sangen]
    return np.random.choice(sang)
