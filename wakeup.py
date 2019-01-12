""""
authors: Micah Mitchell and Josh Mitchell
date 1/12/2019

this program is an automatic loader for the ava website.

note: prior to running this program must run this command pip install pyopenssl ndg-httpsclient pyasn1

run program with this command: python3 wakeup.py
"""
import requests
r = requests.get('https://avalearner2.azurewebsites.net')

print(r.status_code)
print(r.content)