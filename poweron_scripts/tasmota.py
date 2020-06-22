#!/bin/python3

import sys
import urllib.request
import urllib.parse


def setAutoOffRule(addr, event_name, delay_minutes):
	rule = "ON Event#{event_name} DO Power ON ENDON ON Event#{event_name} DO RuleTimer1 {delay} ENDON ON Rules#Timer=1 DO Power1 off ENDON".format(event_name=event_name, delay=delay_minutes*60)
	payload = urllib.parse.quote(rule)
	urllib.request.urlopen("http://{}/cm?cmnd=Rule1%20{}".format(addr, payload))


addr=sys.argv[1]

if sys.argv[2] == "on":
  setAutoOffRule(addr, "auto_off", 15)
  urllib.request.urlopen("http://{}/cm?cmnd=Event%20auto_off".format(addr))

if sys.argv[2] == "off":
  urllib.request.urlopen("http://{}/cm?cmnd=Power%20Off".format(addr))
  

