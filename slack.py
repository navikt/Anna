import os
import schedule
import time
import logging
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

logging.basicConfig(level=logging.DEBUG)


def sendMessage(slack_client, msg, thread_ts=None, channel='#faggruppe_nlp_anna'):
    # make the POST request through the python slack client

    # check if the request was a success
    try:
        slack_client.chat_postMessage(
            channel=channel,
            text=msg,
            thread_ts=thread_ts
        )  # .get()
    except SlackApiError as e:
        logging.error('Request to Slack API Failed: {}.'.format(e.response.status_code))
        logging.error(e.response)

def readLatestMessage(channel_id, slack_client, latest_ts = None):
    # Store conversation history
    conversation_history = []

    try:
        # Call the conversations.history method using the WebClient
        # conversations.history returns the first 100 messages by default
        # These results are paginated, see: https://api.slack.com/methods/conversations.history$pagination
        result = slack_client.conversations_history(channel=channel_id, limit=1, latest=latest_ts)

        conversation_history = result["messages"]
        return conversation_history[0]

    except SlackApiError as e:
        pass