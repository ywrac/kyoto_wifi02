#!/usr/bin/env python
import requests
from random import choice
from passcodes import CODE

s = requests.Session()
s.get('https://login.inf-kyoto-city.info/')
r = s.post('https://login.inf-kyoto-city.info/', data={'passcode': CODE})
