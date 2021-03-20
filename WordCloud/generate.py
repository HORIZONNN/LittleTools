#-*-coding:utf-8—-*-

import argparse
import sys

import jieba.analyse
from wordcloud import WordCloud,ImageColorGenerator
import imageio
import matplotlib.pyplot as plt


def gen_word_cloud(args):
    """
    txt_file : a txt file which contain the content to extract keywords.
    img_file : the name of the background image.
    font_file : the font file (if the content is chinese, it's needed)
    numOfK : the number of keywords
    """
    with open(args.txt_file,'r') as f:
        content = f.read()
    tags = jieba.analyse.extract_tags(content, topK=args.max_words)
    tags = ' '.join(tags) #把分词链接起来，加空格因为英文靠空格分词
    background_img = imageio.imread(args.back_file) if args.back_file != None else None
    wc = WordCloud(width=args.size[0], height=args.size[1], font_path=args.font_file,
        background_color=args.back_color, max_words=args.max_words, mask=background_img,
        max_font_size=args.max_font_size)

    word_cloud = wc.generate(tags)
    plt.imshow(word_cloud)
    plt.axis("off")
    plt.savefig(args.out_file)
    plt.show()
 
 
if __name__=='__main__':

    word2image("吐了")
    sys.exit()

    parser = argparse.ArgumentParser(prog="Txt2Cloud", 
        description="A word cloud generator.")
    parser.add_argument("txt_file", type=str, help="The path of the content file.")
    parser.add_argument("--out_file", type=str, default="wordCloud.png")
    parser.add_argument("--back_file", type=str, help="The path of the background image file.")
    parser.add_argument("--back_color", type=str, default="white")
    parser.add_argument("--font_file", type=str, help="The path of the font file.", default=None)
    parser.add_argument("--size", type=int, nargs=2, default=[2000, 1000])
    parser.add_argument("--max_words", type=int, default=100)
    parser.add_argument("--max_font_size", type=int, default=1000)
    parser.add_argument("--mode", type=str, choices=['ARGB', 'RGB'], default='RGB')
    gen_word_cloud(parser.parse_args())