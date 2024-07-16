#!/usr/bin/python3
'''Convert mardown to html
    functions:
        match_header(num:int, text:str)
        _header(text:str)
'''
if __name__ == "__main__":
    import sys
    import os

    def match_header(num, text):
        '''match header level

            num(int):
                    header level

            text(str):
                    header text

            return(str):
                html string
        '''
        if num == 1:
            return f"<h1>{text}</h1>\n"
        elif num == 2:
            return f"<h2>{text}</h2>\n"
        elif num == 3:
            return f"<h3>{text}</h3>\n"
        elif num == 4:
            return f"<h4>{text}</h4>\n"
        elif num == 5:
            return f"<h5>{text}</h5>\n"
        elif num == 6:
            return f"<h6>{text}</h6>\n"

    def _heading(text):
        '''handinle markdown heading
            text(str):
                markdown text

            return(str):
                string of html
        '''

        html_string = ''
        for line in text:
            tokens = line.split(" ")
            h_lvl = len(tokens[0])
            html_string = html_string+match_header(h_lvl, line[h_lvl+1:-1])
        return html_string

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
