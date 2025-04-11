#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json

zone_ID = '4000000'
API_token = 'supersecrettoken'
API_URI = 'https://dynv6.com/api/v2/zones/' + zone_ID + '/records'
API_header = {'Authorization': 'Bearer ' + API_token, 'content-type': 'application/json'}

my_post =  requests.get(url=API_URI,headers=API_header)
my_reply = my_post.content.decode('utf-8')
json_object = json.loads(my_reply)
print(json.dumps(json_object, indent=4, sort_keys=True))
