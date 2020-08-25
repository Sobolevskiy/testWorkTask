from modules.process_functions import read_json, json_to_html, write_html


def main():
    json_data = read_json()
    html_string = json_to_html(json_data)
    write_html(html_string)


if __name__ == '__main__':
    main()
