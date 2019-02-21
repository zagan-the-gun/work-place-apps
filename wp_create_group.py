#!/bin/python3.6
# -*- coding: utf8 -*-

"""
Overview:
  Create group

Usage:
  wp_create_group.py [-n|--name <NAME>] [-p|--privacy <PRIVACY>] [-v|--verbose] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>]

Options:
  -n --name <NAME>              NAME
  -p --privacy <PRIVACY>        CLOSED OPEN SECRET
  -v --verbose                  Show more information
  -i --id <APP_ID>              APP_ID
  -s --secret <APP_SECRET>      APP_SECRET
  -t --token <ACCESS_TOKEN>     ACCESS_TOKEN
  -c --community <COMMUNITY_ID> COMMUNITY_ID
"""

#(-m|--members <MEMBERS>...) 
#  -m --members <MEMBERS>        MEMBERS

import requests
import json
import datetime
import random
from docopt import docopt
import os
import sys

args = docopt(__doc__)

if args["--name"]:
    NAME = args["--name"][0]
elif os.environ.get('NAME'):
    NAME = os.environ.get('NAME')
else:
    sys.stderr.write("ERROR: --name or NAME not found")
    sys.exit(2)

if args["--privacy"]:
    PRIVACY = args["--privacy"][0]
elif os.environ.get('PRIVACY'):
    PRIVACY = os.environ.get('PRIVACY')
else:
    sys.stderr.write("ERROR: --privacy or PRIVACY not found")
    sys.exit(2)

#if args["--members"]:
#    MEMBERS = args["--members"][0]
#elif os.environ.get('MEMBERS'):
#    MEMBERS = os.environ.get('MEMBERS')
#else:
#    sys.stderr.write("ERROR: --members or MEMBERS not found")
#    sys.exit(2)

if args["--id"]:
    APP_ID = args["--id"][0]
elif os.environ.get('APP_ID'):
    APP_ID = os.environ.get('APP_ID')
else:
    sys.stderr.write("ERROR: --id or APP_ID not found")
    sys.exit(2)

if args["--secret"]:
    APP_SECRET = args["--secret"][0]
elif os.environ.get('APP_SECRET'):
    APP_SECRET = os.environ.get('APP_SECRET')
else:
    sys.stderr.write("ERROR: --secret or APP_SECRET not found")
    sys.exit(2)

if args["--token"]:
    ACCESS_TOKEN = args["--token"][0]
elif os.environ.get('ACCESS_TOKEN'):
    ACCESS_TOKEN = os.environ.get('ACCESS_TOKEN')
else:
    sys.stderr.write("ERROR: --token or ACCESS_TOKEN not found")
    sys.exit(2)

if args["--community"]:
    COMMUNITY_ID = args["--community"][0]
elif os.environ.get('COMMUNITY_ID'):
    COMMUNITY_ID = os.environ.get('COMMUNITY_ID')
else:
    sys.stderr.write("ERROR: --community or COMMUNITY_ID not found")
    sys.exit(2)

GRAPH_URL_PREFIX = "https://graph.facebook.com/"
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

#グループを作成
graph_url = GRAPH_URL_PREFIX + "/community/groups?name=" + NAME + "&description=スポットグループ&privacy=" + PRIVACY
result = requests.post(graph_url, headers=headers)
if result.status_code != requests.codes.ok:
    sys.stderr.write("ERROR: request failed")
    sys.exit(4)
result_json = json.loads(result.text)
group_id = result_json['id']

print("グループID:{}".format(group_id))
print("グループ名:{}".format(NAME))
print("privacy:{}".format(PRIVACY))

sys.exit(0)

