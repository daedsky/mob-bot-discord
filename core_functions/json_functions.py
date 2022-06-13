import json


def read_json(fp):
    with open(fp, 'r') as f:
        x = json.load(f)
        return x


def write_json(fp, data):
    with open(fp, 'w') as f:
        y = json.dumps(data, indent=4)
        f.write(y)
