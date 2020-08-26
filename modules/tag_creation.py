def tag_creator(tag):
    tag_params = ""
    tag_name, tag_classes, tag_id = get_tag_parameters(tag)
    if tag_id:
        tag_params += f' id="{str(tag_id)}"'
    if tag_classes:
        classes = ""
        for tag_class in tag_classes:
            classes += str(tag_class)+' '
        classes = classes.strip()
        tag_params += f' class="{classes}"'

    return tag_name, tag_params


def get_tag_parameters(tag):
    tag_classes = None
    tag_id = None
    if '#' in tag:
        tag = tag.split('#')
        tag_id = tag.pop()
        tag = tag[0]
    if '.' in tag:
        tag_classes = tag.split('.')
        tag_name = tag_classes.pop(0)
    else:
        tag_name = tag
    return tag_name, tag_classes, tag_id
