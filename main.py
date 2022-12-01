#!/usr/bin/env python3
import os
from time import sleep

from slack_sdk import WebClient

import slack
from anna import Anna
# TODO
# må finne 'ts' til meldinger https://api.slack.com/messaging/retrieving#individual_messages
# sende slack-meldingen til anna
# anna svarer
# sende anna sitt svar til tråden:: https://api.slack.com/messaging/sending#threading

anna = Anna()
SLACK_BOT_TOKEN = os.environ['SLACK_BOT_TOKEN']
slack_client = WebClient(SLACK_BOT_TOKEN)
latest_ts = None

svar = 0
while svar < 5:
    meldingFraSlack = slack.readLatestMessage("C045G7VFYA0", slack_client, latest_ts)
    if meldingFraSlack is not None:
        svarFraAnna = anna.svarar(melding=meldingFraSlack['text'])
        slack.sendMessage(slack_client, msg=svarFraAnna, thread_ts=meldingFraSlack['ts'], channel="#faggruppe_nlp_anna")
        latest_ts = meldingFraSlack['ts']
        svar += 1
    sleep(10)
