import json

data = '''{
    "name": "Hypo",
    "Phone": {
        "type": "intl",
        "number": "+1 734 303 4456"
    },
    "email": {
        "hide": "yes"
    }
}'''

info = json.loads(data) #parsing
print(info)
print(type(info))
print("--------------------------------------------")
print('Name:', info["name"])
print("Hide: ", info["email"]["hide"])
