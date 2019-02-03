def format_comment(data):

    comment = ''
    comment += '# ' + data['title'] + '\n\n'
    comment += '# ' + data['body'] + '\n\n'

    return comment