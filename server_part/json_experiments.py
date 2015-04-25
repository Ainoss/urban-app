import json

mydict = [{"dsad":5},{"fdsadf":4},{"dd":33}]

print mydict
print
print json.dumps(mydict)[1]
print
print json.loads(json.dumps(mydict))[1]