#!/usr/bin/env python3
from slack_sdk import WebClient

import slack
from anna import Anna
# TODO
# må finne 'ts' til meldinger https://api.slack.com/messaging/retrieving#individual_messages
# sende slack-meldingen til anna
# anna svarer
# sende anna sitt svar til tråden:: https://api.slack.com/messaging/sending#threading
from config import SLACK_BOT_TOKEN
meldingFraSlack = "varför kom du inte?: "
anna = Anna()
svarFraAnna = anna.svarar(melding=meldingFraSlack)
slack.sendMessage(WebClient(SLACK_BOT_TOKEN), msg=svarFraAnna, thread_ts='1668682105.635539', channel="#faggruppe_nlp")
