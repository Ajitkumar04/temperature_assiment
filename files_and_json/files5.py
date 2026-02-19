# JSON - like dictionmary:
import json
preson ={"name":"ajit",
         "age":21,
         "city":"darbhang",
         "skills":["python","AL-MI"]}
json_strig=json.dumps(preson,indent=2)
print(json_strig)
print(type(preson))
print(type(json_strig))