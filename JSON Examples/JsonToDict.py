import json

jsonString = '{"a":54, "b": {"c":87}}'
aDict = json.loads(jsonString)
print(aDict)
print(aDict['a'])
print(aDict['b'])
print(aDict['b']['c'])