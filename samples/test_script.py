# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 11:48:16 2018

@author: michael
"""

#%reset -f

import json
from my_functions import login, listObjects, printeverything, createObject, getObject, deleteObject, updateObject

payload = {
            "username": 'michael',
            "password": 'password123'
}

token = login('michael','password123')

r = listObjects(token)
printeverything(r)
d = r.json()

with open('risktype_l1.json') as f1:
    data1 = json.load(f1)
    
with open('risktype_l2.json') as f2:
    data2 = json.load(f2)

with open('risktype_l3.json') as f3:
    data3 = json.load(f3)

with open('risktype_l3_err.json') as f3:
    data_err = json.load(f3)




r = createObject(token, data1)
printeverything(r)


r = createObject(token, data2)
printeverything(r)


r = createObject(token, data3)
printeverything(r)

#Should give you 404 and roll back, don't want weird stuff in db
r = createObject(token, data_err)
printeverything(r)


r = getObject(token, 50)
printeverything(r)
edit_data = None
edit_data = r.json()

r = updateObject(token, 50, edit_data)
printeverything(r)


for i in range(40,49):
    print(i)
    r = deleteObject(token, i)
    printeverything(r)