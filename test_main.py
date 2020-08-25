from modules.process_functions import json_to_html


def test_html_string_creation():
    data = [{"title": "testTitle", "body": "testBody"}]
    func = json_to_html(data)
    assert func == '<h1>testTitle</h1><p>testBody</p>'
