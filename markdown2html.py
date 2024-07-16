#!/usr/bin/python3
'''Convert mardown to html
    functions:
        match_header(num:int, text:str)
        _header(text:str)
'''
if __name__ == "__main__":
    import sys
    import os

    def write_file(val, file_name):
        '''write lines to a file
        val(str):
            line to write

            file_name(str):
                name of file to write into
        '''
        with open(file_name, 'a', encoding="utf-8") as fp:
            fp.write(val)

    def match_header(num, text, file):
        '''match header level

            num(int):
                    header level

            text(str):
                    header text

            return(str):
                html string
        '''
        if num == 1:
            write_file(f"<h1>{text}</h1>\n", file)
        elif num == 2:
            write_file(f"<h2>{text}</h2>\n", file)
        elif num == 3:
            write_file(f"<h3>{text}</h3>\n", file)
        elif num == 4:
            write_file(f"<h4>{text}</h4>\n", file)
        elif num == 5:
            write_file(f"<h5>{text}</h5>\n", file)
        elif num == 6:
            write_file(f"<h6>{text}</h6>\n", file)

    def _heading(text, file):
        '''handinle markdown heading
            text(str):
                markdown text

            return(str):
                string of html
        '''
        for line in text:
            if line is not "\n":
                tokens = line.split(" ")
                h_lvl = len(tokens[0])
                match_header(
                    h_lvl,
                    line[h_lvl+1:-1],
                    file
                )

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
        html = _heading(mkdown, html_file)
