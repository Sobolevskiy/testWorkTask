import json


def read_json(path_to_json='data/source.json'):
    with open(path_to_json, 'r') as json_file:
        data = json.loads(json_file.read())
    return data


def json_to_html(data):
    ans = ""
    for i in data:
        ans += "<h1>" + i["title"] + "</h1>"
        ans += "<p>" + i["body"] + "</p>"
    return ans


def write_html(html_str, path_to_html='data/index.html'):
    with open(path_to_html, 'w') as html_file:
        html_file.write(html_str)
