import win32clipboard as w
import win32con
import argparse
import sys


def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()

if __name__ == "__main__":
    # parse = argparse.ArgumentParser()
    # parse.add_argument("--content", required=True)
    # parse.add_argument("--toup", action='store_true', default=False, help="fffff")
    # parse.add_argument("--tolow", action='store_true', default=False)
    # parse.add_argument("--tocap", action='store_true', default=False)
    # parse.add_argument("--totit", action='store_true', default=False)

    # args = parse.parse_args()

    # convert_content = args.content

    convert_type = sys.argv[1]
    convert_content = sys.argv[2]

    if convert_type == "up":
        convert_content = convert_content.upper()
    if convert_type == "low":
        convert_content = convert_content.lower()
    if convert_type == "cap":
        convert_content = convert_content.capitalize()
    if convert_type == "tit":
        convert_content = convert_content.title()

    set_text(convert_content)
