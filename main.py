# ACA Warriors App Bot: warriors_bot
import logging
import os
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

logging.basicConfig(level=logging.INFO)
load_dotenv()

SLACK_BOT_TOKEN = os.environ["ACA_Warriors_App_Bot_User_OAuth_Token"]
SLACK_APP_TOKEN = os.environ["ACA_Warriors_App_Socket_Mode_Token"]

app = App(token=SLACK_BOT_TOKEN)

@app.event("app_mention")
def mention_handler(body, context, payload, options, say, event):
    say("Let's Go Warriors!")

@app.event("message")
def mention_handler(body, context, payload, options, say, event):
    pass

if __name__ == '__main__':
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
