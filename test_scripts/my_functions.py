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

def printeverything(r):
    print("Status:\t", r.status_code)
    try:
        res = r.json()
        print(res)
    except JSONDecodeError:
        print("Failed to Convert response to json")
        
    
def login(username,password):
    baseUrl = "http://localhost:8000"
    loginUrl = baseUrl + '/api-token-auth/'
    
    #
    headers = {
            "Content-Type": "application/json"
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
    url = "http://localhost:8000/risk-types/"
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + token
    }
    r = requests.post(url, headers = headers, data= json.dumps(data))
    #res = r.json()
    return r

def updateObject(token, objectId, data):
    url = "http://localhost:8000/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + token
    }
    r = requests.put(url, headers = headers, data= json.dumps(data))
    #res = r.json()
    return r

def listObjects(token):
    url = "http://localhost:8000/risk-types/"
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + token
    }
    r = requests.get(url, headers = headers)
    #res = r.json()
    return r

def getObject(token, objectId):
    url = "http://localhost:8000/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + token
    }
    r = requests.get(url, headers = headers)
    #res = r.json()
    return r 

def deleteObject(token, objectId):
    url = "http://localhost:8000/risk-types/" + str(objectId) + '/'
    
    headers = {
            "Content-Type": "application/json",
            "Authorization": "token " + token
    }
    r = requests.delete(url, headers = headers)
    #res = r.json()
    return r 

