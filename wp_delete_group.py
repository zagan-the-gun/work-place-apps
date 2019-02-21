#!/bin/python3.6
# -*- coding: utf8 -*-

"""
Overview:
  delete groups

Usage:
  wp_delete_group.py [<GROUP_IDS>...] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>] [-f|--force <DUMMY_USER_ID>]

Options:
  <GROUP_IDS>                   group ids
  -i --id <APP_ID>              APP_ID
  -s --secret APP_SECRET        APP_SECRET
  -t --token <ACCESS_TOKEN>     ACCESS_TOKEN
  -c --community <COMMUNITY_ID> COMMUNITY_ID
  -f --force <DUMMY_USER_ID>    forcibly delete group
"""

import requests
import json
from docopt import docopt
import os
import sys

args = docopt(__doc__)

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

if args["--force"]:
    DUMMY_USER_ID = args["--force"][0]
elif os.environ.get('DUMMY_USER_ID'):
    DUMMY_USER_ID = os.environ.get('DUMMY_USER_ID')
else:
    DUMMY_USER_ID = "";

GRAPH_URL_PREFIX = "https://graph.facebook.com/"
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

#グループを削除
for group_id in args['<GROUP_IDS>']:
    #グループのメンバー取得
    graph_url = GRAPH_URL_PREFIX + group_id + "/members?limit=3000&fields=id,name,email"
    result = requests.get(graph_url, headers=headers)
    if result.status_code != requests.codes.ok:
        sys.stderr.write("ERROR: request failed")
        sys.exit(4)
    result_json = json.loads(result.text)
    group_members = result_json['data']

    #メンバーがいる場合は全員削除
    if group_members is not None:
        for member in group_members:
            graph_url = GRAPH_URL_PREFIX + "/" + group_id + "/members/" + member['id']
            result = requests.delete(graph_url, headers=headers)
            if result.status_code != requests.codes.ok:
                sys.stderr.write("ERROR: request failed")
                sys.exit(4)
            result_json = json.loads(result.text)

    #メンバーがいない場合はダミーを追加してから削除
    if (((group_members is None) or (len(group_members) <= 0)) and (DUMMY_USER_ID is not None)):
        #ダミーを追加
        graph_url = GRAPH_URL_PREFIX + "/" + group_id + "/members/" + DUMMY_USER_ID
        result = requests.post(graph_url, headers=headers)
        if result.status_code != requests.codes.ok:
            sys.stderr.write("ERROR: request failed")
            sys.exit(4)
        result_json = json.loads(result.text)

        #ダミーを削除
        graph_url = GRAPH_URL_PREFIX + "/" + group_id + "/members/" + DUMMY_USER_ID
        result = requests.delete(graph_url, headers=headers)
        if result.status_code != requests.codes.ok:
            sys.stderr.write("ERROR: request failed")
            sys.exit(4)
        result_json = json.loads(result.text)

sys.exit(0)

