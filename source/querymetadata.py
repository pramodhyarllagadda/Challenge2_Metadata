import requests
import json

metadata_url = 'http://169.254.169.254/latest/'


def expand_jsontree(url, arr):
    result = {}
    for item in arr:
        new_url = url + item
        r = requests.get(new_url)
        text = r.text
        if item[-1] == "/":
            list_of_values = r.text.splitlines()
            result[item[:-1]] = expand_jsontree(new_url, list_of_values)
        elif is_valid_json(text):
            result[item] = json.loads(text)
        else:
            result[item] = text
    return result


def metadata():
    path = ["meta-data/"]
    result = expand_jsontree(metadata_url, path)
    return result


def metadata_json():
    md = metadata()
    metadata_json = json.dumps(md, indent=4, sort_keys=True)
    return metadata_json


def is_valid_json(value):
    try:
        json.loads(value)
    except ValueError:
        return False
    return True


if __name__ == '__main__':
    print(metadata_json())
[root@ip-172-31-86-59 source]# cat querymetadata.py
from metadata import metadata


def gen_dict_extract(key, var):
    if hasattr(var, 'items'):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in gen_dict_extract(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in gen_dict_extract(key, d):
                        yield result


def find_key(key):
    md = metadata()
    return list(gen_dict_extract(key, md))


if __name__ == '__main__':
    key = input("Enter the key name to get the value\n")
    print(find_key(key))
