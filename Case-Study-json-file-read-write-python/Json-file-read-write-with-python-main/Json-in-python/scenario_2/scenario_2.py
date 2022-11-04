import json
from glob import glob

output = []
for jsonFile in glob('jsons/*.png.json'):
    f = open(jsonFile)
    data = json.loads(f.read())
    for i in data['objects']:
        if i['classTitle'].lower() == 'vehicle':
            i['classTitle'] = 'Car'
        elif i['classTitle'].lower() == 'license plate':
            i['classTitle'] = 'Number'

    output.append(data)
    # f.close()

with open('combined_json.json', 'w') as f:
    json.dump(output, f)
