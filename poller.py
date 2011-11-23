#!/usr/bin/env python

import json
import time
import urllib2

USER = '' # couch user name
PASSWD = '' # password

COUCH = "http://127.0.0.1:5984/"
DB = 'candyminds/'

password_mgr = urllib2.HTTPPasswordMgr()
password_mgr.add_password(None, COUCH, USER, PASSWD)
handler = urllib2.HTTPBasicAuthHandler(password_mgr)
opener = urllib2.build_opener(handler)
opener.open(COUCH)
urllib2.install_opener(opener)

stored_ip = "www.cakewrecks.com"

while True:
    try:
        current_ip = urllib2.urlopen('http://www.whatismyip.org', timeout=10).read()
        if current_ip != stored_ip:
            stored_ip = current_ip
            doc = urllib2.urlopen(COUCH + DB + 'current_ip_address', timeout=10).read()
            doc = json.loads(doc)
            doc['latest'] = current_ip
            request = urllib2.Request(COUCH + DB, json.dumps(doc))
            request.add_header('Content-Type', 'application/json')
            response = urllib2.urlopen(request)
        time.sleep(7200)
    except: # try again in a few hours
        time.sleep(7200)
