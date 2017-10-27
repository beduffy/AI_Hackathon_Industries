#!/usr/bin/env python
"""
Minimal Example
===============
Generating a square wordcloud from the US constitution using default arguments.
"""

import sys
import os
from os import path
import numpy as np
from PIL import Image
import argparse

def create_word_cloud(text, output_image_fp):
    word_cloud_dir = 'C:\\Users\\benjamin.duffy\\Downloads\\wordcloud-1.3.1.tar\\wordcloud-1.3.1'
    #os.chdir(word_cloud_dir)

    sys.path.insert(0, word_cloud_dir)

    d = path.dirname(__file__)
    print('dirname:', d)
    print('cwd:', os.getcwd())


    from wordcloud import WordCloud

    # read the mask / color image taken from
    # http://jirkavinse.deviantart.com/art/quot-Real-Life-quot-Alice-282261010
    '''alice_coloring = np.array(Image.open(path.join(d, "alice_color.png")))
    stopwords = set(STOPWORDS)
    stopwords.add("said")

    wc = WordCloud(background_color="white", max_words=2000, mask=alice_coloring,
                   stopwords=stopwords, max_font_size=40, random_state=42)
    # generate word cloud
    wc.generate(text)

    # create coloring from image
    image_colors = ImageColorGenerator(alice_coloring)

    # show
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    # recolor wordcloud and show
    # we could also give color_func=image_colors directly in the constructor
    plt.imshow(wc.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")
    plt.figure()
    plt.imshow(alice_coloring, cmap=plt.cm.gray, interpolation="bilinear")
    plt.axis("off")
    plt.show()

    # Read the whole text.
    #text = open(path.join(d, 'constitution.txt')).read()
    sys.exit()'''
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
    #plt.show()


    plt.savefig(output_image_fp)

    # The pil way (if you don't have matplotlib)
    # image = wordcloud.to_image()
    # image.show()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='')
    args = parser.parse_args()
