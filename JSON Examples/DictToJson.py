#!/usr/bin/python

#############################################################################################################
# Python dictionary to JSON example                                                                         #
#############################################################################################################



import json

# Data to be written
dictionary = {
    "id": "04",
    "name": "sunil",
    "department": "HR"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)
print(json_object)