import json

with open('users.json', 'r') as f:
    data = json.load(f)


newdata = ''

for i, j in enumerate(data):
    newdata += f'{i} ' + str(j)
    newdata += '\n'

with open('users.txt', 'w')as f:
    json.dump(newdata, f, ensure_ascii=False)


print(newdata)