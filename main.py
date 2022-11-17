#!/usr/bin/env python3
import os

from slack_sdk import WebClient

import scheduled_message
from anna import Anna

channel = '#faggruppe_nlp_anna'
#while True:
#Anna().hej()

if __name__ == '__main__':
    client = WebClient(os.environ['SLACK_BOT_TOKEN'])
    #client.channels_setTopic(channel=channel, topic='Jag är en topic!')
    #foo = client.conversations_history(channel=channel)
    client.chat_postMessage(channel=channel,
            text="...",
            attachments='''[
            {
            "fallback": "Ojsann!",
            "image_url": "https://a.cockfile.com/ivMDdR.jpeg"
            }]'''
            )
