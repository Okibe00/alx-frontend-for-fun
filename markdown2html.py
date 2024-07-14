#!/usr/bin/python3
'''Convert mardown to html
'''
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
    exit(0)
    with open(markdown_file, 'r', encoding="utf-8") as fp:
        mkdown = fp.read()

    with open(html_file, 'w', encoding="utf-8") as fp:
        fp.write(mkdown)
        exit(0)
