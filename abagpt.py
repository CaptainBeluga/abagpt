import json
import secrets
import string

question = input("question => ").lower()

for sy in string.punctuation:
    question = question.replace(sy,"")

options = []

f = dict(json.loads(open("questions.json","r").read()))


for bruh in f.keys():
    options.append(bruh)


possible = []
for op in options:
    Sop = op.split("-")
    
    for x in Sop:
        if x in question:
            if op not in possible:
                possible.append(op)

print(possible)

if(len(possible) > 0):
    x = f[secrets.choice(possible)]


    if len(x) > 1 and str(type(x)) == "<class 'list'>":
        print(secrets.choice(x))

    else:
        print(x)

else:
    print(secrets.choice(f["default_message"]))