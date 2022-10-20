#!/usr/bin/env python3
import os

from slack_sdk import WebClient

import scheduled_message
from anna import Anna

#while True:
#Anna().hej()
scheduled_message.sendMessage(WebClient(os.environ['SLACK_BOT_TOKEN']), "God eftermiddag!")
