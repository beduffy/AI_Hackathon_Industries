#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import sys
import os
from os import path
import argparse

def create_word_cloud(text):
    word_cloud_dir = 'C:\\Users\\benjamin.duffy\\Downloads\\wordcloud-1.3.1.tar\\wordcloud-1.3.1'
    #os.chdir(word_cloud_dir)

    sys.path.insert(0, word_cloud_dir)

    d = path.dirname(__file__)
    print('dirname:', d)
    print('cwd:', os.getcwd())


    from wordcloud import WordCloud



    # Read the whole text.
    #text = open(path.join(d, 'constitution.txt')).read()

    # Generate a word cloud image
    wordcloud = WordCloud().generate(text)

    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")

    # lower max_font_size
    wordcloud = WordCloud(max_font_size=40).generate(text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # image.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='Audio file to be recognized')
    args = parser.parse_args()
