#!/bin/python3.6
# -*- coding: utf8 -*-

from flask import Flask, request
import requests
import json
import os
import sys
import urllib.parse

app = Flask(__name__)

VERIFY_TOKEN = ''

CHATWORK_TOKEN = ""
CHATWORK_URL_PREFIX = "https://api.chatwork.com/v2/"
CHATWORK_ROOM = ""
chatwork_headers = {'X-ChatWorkToken': CHATWORK_TOKEN}

SLACK_URL_PREFIX = ""
SLACK_CHANNEL = ""
SLACK_NAME = ""

@app.route('/', methods=['GET'])
def handle_verification():
    if (request.args.get('hub.verify_token', '') == VERIFY_TOKEN):
        print("Verified")
        return request.args.get('hub.challenge', '')
    else:
        print("Wrong token")
        return "Error, wrong validation token"

@app.route('/', methods=['POST'])
def handle_message():
    '''
    Handle messages sent by facebook messenger to the applicaiton
    '''

    data = request.get_json()

    if data["object"] == "group":
        for entry in data["entry"]:
            for messaging_event in entry["changes"]:
                if messaging_event.get("value"):
                    value = messaging_event.get('value')

                    from_name = value["from"]["name"]
                    message = value["message"]
                    permalink_url = value["permalink_url"]

                    body = "差出人: {}\n".format(from_name) + "メッセージ: {}\n".format(message) + permalink_url
                    body_urlencode = urllib.parse.quote("差出人: {}\n".format(from_name) + "メッセージ: {}\n".format(message) + permalink_url)

    #Chatwork 送信
    chatwork_url = CHATWORK_URL_PREFIX + "rooms/" + CHATWORK_ROOM + "/messages?body=" + body_urlencode
    result = requests.post(chatwork_url, headers=chatwork_headers)
    if result.status_code != requests.codes.ok:
        sys.stderr.write("chatwork error!")
        sys.exit(4)

    #Slack 送信
    payload = {}
    payload["channel"] = SLACK_CHANNEL
    payload["username"] = SLACK_NAME
    payload["text"] = body
    payload_json = json.dumps(payload)

    slack_url = SLACK_URL_PREFIX
    print(slack_url)
    result = requests.post(slack_url, data=payload_json)
    print(result)
    if result.status_code != requests.codes.ok:
        sys.stderr.write("chatwork error!")
        sys.exit(4)

    return "ok"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')

