# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 15:05:21 2018

@author: nicolas
"""
import urllib
import json
#https://stackoverflow.com/questions/34740288/importerror-no-module-named-urllib2-python-3/34740459

def get_temperature():
    return 10

def get_humidity():
    return 11

def get_pressure():
    return 12
    
# Get Raspberry Pi Public IP via IPIFY Rest Call
def get_public_ip():
  ip = json.load(urllib.urlopen('https://api.ipify.org/?format=json'))['ip']
  return ip