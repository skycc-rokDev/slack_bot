# -*- coding: utf-8 -*-
import json
from flask import Flask, request, make_response
from slacker import Slacker

token = "YOUR_BOT_TOKEN" #Bot

slack = Slacker(token)

app = Flask(__name__)

def get_answer(user_query):
    return user_query

def event_handler(event_type, slack_event):

    channel = slack_event["event"]["channel"]

    string_slack_event = str(slack_event)

    if string_slack_event.find("{'type': 'user', 'user_id': ") != -1:  # 멘션으로 호출

        try:

            user_query = slack_event['event']['blocks'][0]['elements'][0]['elements'][1]['text']

            answer = get_answer(user_query)

            slack.chat.post_message(channel, answer)

            return make_response("ok", 200, )

        except IndexError:

            pass

    message = "[%s] cannot find event handler" % event_type

    return make_response(message, 200, {"X-Slack-No-Retry": 1})


@app.route('/', methods=['POST'])

def hello_there():

    slack_event = json.loads(request.data)

    if "challenge" in slack_event:

        return make_response(slack_event["challenge"], 200, {"content_type": "application/json"})

    if "event" in slack_event:

        event_type = slack_event["event"]["type"]

        return event_handler(event_type, slack_event)

    return make_response("There are no slack request events", 404, {"X-Slack-No-Retry": 1})





if __name__ == '__main__':

    app.run(debug=True)