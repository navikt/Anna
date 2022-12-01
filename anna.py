import numpy as np
stoppord = ["anna", "bot"]

class Anna:
    def hej(self):
        # fråga = inmatning(input())
        # if "bot" in fråga:
        #     print("Jag är ingen bot! Jag är en väldigt, väldigt vacker tjej")
        # else:
        return slumpmassigtSvar()

    def svarar(self, melding):
        return rensare(melding) + " " + slumpmassigtSvar()

def inmatning(text: str):
    # todo rense teksten
    # todo vektorisere
    return rensare(text)


def rensare(text: str):
    rensade_text = text.lower()
    # todo fjerne andre tegn en ?
    text_utan_stoppord = [ord.replace("?", "") for ord in rensade_text.split(" ") if ord not in stoppord]
    return " ".join(text_utan_stoppord)


def slumpmassigtSvar():
    with open("boten_anna.txt", "r") as f:
        sangen = f.readlines()

    sang = [linje.replace("\n", "") for linje in sangen]
    return np.random.choice(sang)
