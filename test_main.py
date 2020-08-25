from modules.process_functions import json_to_html


def test_html_string_creation():
    data = [{"h3": "Title #1", "div": "Hello, World 1!"}]
    func = json_to_html(data)
    assert func == '<h3>Title #1</h3><div>Hello, World 1!</div>'
