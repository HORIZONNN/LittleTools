import win32clipboard as w
import win32con
import argparse
import sys
import pygame
import pypinyin


def set_text(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


def title2Title(convert_content, convert_type):
    if convert_type == "up":
        convert_content = convert_content.upper()
    if convert_type == "low":
        convert_content = convert_content.lower()
    if convert_type == "cap":
        convert_content = convert_content.capitalize()
    if convert_type == "tit":
        convert_content = convert_content.title()

    return convert_content
    set_text(convert_content)


def word2image(word):
    pygame.init()
    font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuibold', 64, True)
    ftext = font.render(word, True, (65, 83, 130),(255, 255, 255))
    pygame.image.save(ftext, "image.png")

def word2pinyin(word):
    result = []
    # heteronym开启多音字
    pinyin = pypinyin.pinyin(word, heteronym=False)
    for i in pinyin:
        result.extend(i)
    return " ".join(result)

if __name__ == "__main__":
    # parse = argparse.ArgumentParser()
    # parse.add_argument("--content", required=True)
    # parse.add_argument("--toup", action='store_true', default=False, help="fffff")
    # parse.add_argument("--tolow", action='store_true', default=False)
    # parse.add_argument("--tocap", action='store_true', default=False)
    # parse.add_argument("--totit", action='store_true', default=False)

    # args = parse.parse_args()

    # convert_content = args.content

    string = title2Title("fdsfdsfds", 'up')

    
