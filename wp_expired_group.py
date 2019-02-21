#!/bin/python3.6
# -*- coding: utf8 -*-

"""
Overview:
  List of expired groups

Usage:
  wp_expired_group.py [-v|--verbose] [-i|--id <APP_ID>] [-s|--secret <APP_SECRET>] [-t|--token <ACCESS_TOKEN>] [-c|--community <COMMUNITY_ID>]

Options:
  -v --verbose                  Show more information
  -i --id=<APP_ID>              APP_ID
  -s --secret <APP_SECRET>      APP_SECRET
  -t --token <ACCESS_TOKEN>     ACCESS_TOKEN
  -c --community <COMMUNITY_ID> COMMUNITY_ID
"""

import requests
import json
import datetime
import re
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

GRAPH_URL_PREFIX = "https://graph.facebook.com/"
headers = {'Authorization': 'Bearer ' + ACCESS_TOKEN}

#現在時刻を取得
NOW = datetime.datetime.now()

# グループ名に日時データが含まれているかチェック
def checkGroupNameDate(group_name):
    try:
        datetime.datetime.strptime(re.sub(r'\D', '', group_name)[0:8], '%Y%m%d') 
        return True
    except ValueError:
        return False

#グループ一覧を取得
graph_url = GRAPH_URL_PREFIX + COMMUNITY_ID + "/groups?limit=1000&fields=name,privacy,updated_time"
result = requests.get(graph_url, headers=headers)
if result.status_code != requests.codes.ok:
    sys.stderr.write("ERROR: request failed")
    sys.exit(4)
result_json = json.loads(result.text)
groups = result_json['data']

#グループ一覧を処理
for group in groups:
    #対象グループ名を抽出
    if group['name'].find("[SPOT", 0, 5) == 0:
        #正しい命名規則のグループは名前の日付で削除処理
        #この方法で抽出は正規表現的にちょっとまずいかも？
        tmp_day = re.sub(r'\D', '', group['name'])[0:8]
        if checkGroupNameDate(group['name']):
            d_day = datetime.datetime.strptime(tmp_day, '%Y%m%d')
            if ((d_day + datetime.timedelta(days=2))-NOW).days <= 0:
                if args["--verbose"] == False:
                    print(group['id'] + " ", end = "")
                else:
                    print(group['id'] + ":" + group['privacy'] + ":" + group['name'])
                    print("    group削除指定日:" + tmp_day)
                    print("    group削除指定日まで {} 日 ".format(((d_day + datetime.timedelta(days=2))-NOW).days))
                    print("")

sys.exit(0)

