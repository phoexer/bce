# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:50:15 2018

@author: michael
"""

import json
import requests
import random
import string
from json import JSONDecodeError


baseUrl = "http://127.0.0.1:8000/api"

def printeverything(r):
    print("Status:\t", r.status_code)
    try:
        res = r.json()
        print(res)
    except JSONDecodeError:
        print("Failed to Convert response to json")
        
    
def login(username,password):
    
    loginUrl = baseUrl + '/api-token-auth/'
    
    #
    headers = {
            "Content-Type": "application/json",
            'X-CSRFToken': '*',
            'X-Frame-Options': '*'
    }
    #Login with new user
    payload = {
            "username": username,
            "password": password
    }
    
    r = requests.post(loginUrl, headers=headers, data = json.dumps(payload))
    printeverything(r)
    
    res = r.json()
    
    token = res["token"]

    return token


def createObject(token, data):
    url = baseUrl + "/risk-types/"
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + token
    }
    r = requests.post(url, headers = headers, data= json.dumps(data))
    #res = r.json()
    return r

def updateObject(token, objectId, data):
    url = baseUrl + "/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + token
    }
    r = requests.put(url, headers = headers, data= json.dumps(data))
    #res = r.json()
    return r

def listObjects(token):
    url = baseUrl + "/risk-types/"
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + token
    }
    r = requests.get(url, headers = headers)
    #res = r.json()
    return r

def getObject(token, objectId):
    url = baseUrl + "/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + token
    }
    r = requests.get(url, headers = headers)
    #res = r.json()
    return r 

def deleteObject(token, objectId):
    url = baseUrl + "/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "JWT " + token
    }
    r = requests.delete(url, headers = headers)
    #res = r.json()
    return r 

