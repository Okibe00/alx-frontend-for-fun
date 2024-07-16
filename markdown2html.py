#!/usr/bin/python3
'''Convert mardown to html
'''


def match_header(num, text):
    '''match header level
    '''

    match num:
        case 1:
            return f"<h1>{text}</h1>\n"
        case 2:
            return f"<h2>{text}</h2>\n"
        case 3:
            return f"<h3>{text}</h3>\n"
        case 4:
            return f"<h4>{text}</h4>\n"
        case 5:
            return f"<h5>{text}</h5>\n"
        case 6:
            return f"<h6>{text}</h6>\n"


def _heading(text):
    '''handinle markdown heading
        line(str): markdown text
        return(str): string of html
    '''
    html_string = ''
    for line in text:
        tokens = line.split(" ")
        html_string = html_string+match_header(len(tokens[0]), tokens[1])
    return html_string


if __name__ == "__main__":
    import sys
    import os

    arg_len = len(sys.argv)
    if arg_len < 3:
        print(
                "Usage: ./markdown2html.py README.md README.html",
                file=sys.stderr
            )
        exit(1)
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]
    if os.path.exists(markdown_file) is False:
        print(f'Missing {markdown_file}', file=sys.stderr)
        exit(1)

    with open(markdown_file, 'r', encoding="utf-8") as fp:
        mkdown = fp.readlines()
        html = _heading(mkdown)

    with open(html_file, 'w', encoding="utf-8") as fp:
        fp.write(html)
        exit(0)
