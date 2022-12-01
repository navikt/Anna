import numpy as np
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

tokenizer = AutoTokenizer.from_pretrained("flax-community/nordic-gpt-wiki")
model = AutoModelForCausalLM.from_pretrained("flax-community/nordic-gpt-wiki")
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
stoppord = ["anna", "bot"]

class Anna:
    def hej(self):
        # fråga = inmatning(input())
        # if "bot" in fråga:
        #     print("Jag är ingen bot! Jag är en väldigt, väldigt vacker tjej")
        # else:
        return slumpmassigtSvar()

    def svarar(self, melding):
        p = np.random.rand(1)
        if p > 0.7:
            return slumpmassigtSvar()
        else:
            svar = generator(melding, num_return_sequences=1, max_length = 100)[0]["generated_text"]
            return " ".join(svar.split(".")[:-1])

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
