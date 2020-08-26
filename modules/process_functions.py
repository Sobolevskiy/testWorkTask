import json
from collections import Iterable
from html import escape
from modules.tag_creation import tag_creator


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
            ans += add_tag(key, datas[key])
    return ans


def write_html(html_str, path_to_html='data/index.html'):
    with open(path_to_html, 'w') as html_file:
        html_file.write(html_str)


def add_tag(tag, data_in_tag):
    tag_name, tag_params = tag_creator(tag)
    if isinstance(data_in_tag, Iterable) and not isinstance(data_in_tag, str):
        text = str(json_to_html(data_in_tag))
    else:
        text = escape(str(data_in_tag))
    return f"<{str(tag_name)+str(tag_params)}>"+text+f"</{str(tag_name)}>"
