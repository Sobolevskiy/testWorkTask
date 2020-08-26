from modules.process_functions import json_to_html, add_tag
from modules.tag_creation import get_tag_parameters


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


def test_nested_list_string_creation():
    data = [{"h3": "Title #1", "div": "Hello, World 1!"},
            [{"h1": "text 1", "div": "text 2"}]]
    func = json_to_html(data)
    result_string = ('<ul><li><h3>Title #1</h3><div>Hello, World 1!</div></li>'
                     '<li><ul><li><h1>text 1</h1><div>text 2</div></li></ul></li></ul>')
    assert func == result_string


def test_get_some_tag_parameters():
    assert get_tag_parameters("p.cl1.cl2") == ("p", ["cl1", "cl2"], None)


def test_get_tag_and_id():
    assert get_tag_parameters("div#id1") == ("div", None, 'id1')


def test_get_tag_and_other_parameters():
    assert get_tag_parameters("p.cl1.cl2#id2") == ("p", ["cl1", "cl2"], 'id2')


def test_get_only_tag():
    assert get_tag_parameters("tag") == ("tag", None, None)


def test_add_tag_and_text():
    func = add_tag('div', 'text<a>Inside</a>')
    assert func == '<div>text&lt;a&gt;Inside&lt;/a&gt;</div>'


def test_add_tag_and_dict_inside():
    func = add_tag('div', {"p": "text"})
    assert func == '<div><p>text</p></div>'
