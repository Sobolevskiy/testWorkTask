from modules.process_functions import json_to_html


def test_html_list_string_creation():
    data = [{"h3": "Title #1", "div": "Hello, World 1!"},
            {"h3": "Title #2", "div": "Hello, World 2!"}]
    func = json_to_html(data)
    assert func == ('<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li>'
                    '<li><h3>Title #2</h3><div>Hello, World 2!</div></li></ul>')


def test_html_not_list_string_creation():
    data = {"h3": "Title", "div": "block"}
    func = json_to_html(data)
    assert func == '<h3>Title</h3><div>block</div>'
