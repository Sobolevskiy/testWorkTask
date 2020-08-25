import json


def read_json(path_to_json='data/source.json'):
    with open(path_to_json, 'r') as json_file:
        data = json.loads(json_file.read())
    return data


def json_to_html(datas):
    ans = ""
    if isinstance(datas, list):
        ans += "<ul>"
        for i in datas:
            ans += '<li>'+json_to_html(i)+'</li>'
        ans += '</ul>'
    else:
        for key in datas:
            ans += f'<{str(key)}>{datas[key]}</{str(key)}>'
    return ans


def write_html(html_str, path_to_html='data/index.html'):
    with open(path_to_html, 'w') as html_file:
        html_file.write(html_str)
