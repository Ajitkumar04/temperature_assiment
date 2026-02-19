import json
json_strig  ='{"name":"bob","age":23,"active":true}'
person =json.loads(json_strig)
print(person)
print(type(person))
print(person["name"])