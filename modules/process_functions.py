import json


def read_json(path_to_json='data/source.json'):
    with open(path_to_json, 'r') as json_file:
        data = json.loads(json_file.read())
    return data


def json_to_html(datas):
    ans = ""
    for data in datas:
        for i in data:
            ans += f'<{str(i)}>{data[i]}</{str(i)}>'
    return ans


def write_html(html_str, path_to_html='data/index.html'):
    with open(path_to_html, 'w') as html_file:
        html_file.write(html_str)
