from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals

import argparse
from collections import Counter
import nltk
from nltk.corpus import stopwords

from transcribe import transcribe_file
import pyteaser_summary
import sentiment

output_folder = 'intermediate_data'

# 2. Audio to text
def audio_to_text(audio_fp):
    transcribe_file(audio_fp, output_folder)

# 3.1 Summarisation
def summarise_text(title, text):
    # todo try sumy, smmry,


    summaries = pyteaser_summary.summarise_text(title, text)

    print('\nSummaries:')
    print(summaries)

    # write to global JSON


# 3.2 Sentiment
def process_sentiment(text):
    sentiment_of_text = sentiment.process_sentiment(text_from_file)

    print ('\nSentiment:')
    print (sentiment_of_text)
# 3.3 Topic Modelling

# 3.4 word cloud
def word_cloud(text):
    s = text
    s_tokens = nltk.word_tokenize(s) #s.split()

    s_tokens = [t for t in s_tokens if not t in stopwords.words('english')]

    print('\nWord Cloud word frequencies:')
    print(Counter(s_tokens).most_common(100))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='Audio file to be recognized')
    args = parser.parse_args()

    global_JSON = {}
    intermediate_fn = 'Nightfall1.txt'
    intermediate_fp = output_folder + '/' + intermediate_fn




    #output_text
    #audio_to_text(args.path)



    audio_text_file_raw = open(intermediate_fp, 'r')
    text_from_file = audio_text_file_raw.read()

    print('Beginning to process text file\n')
    # 3.1
    summarise_text(intermediate_fn, text_from_file)

    # 3.2
    process_sentiment(text_from_file)

    # 3.3

    # 3.4
    word_cloud(text_from_file)



    audio_text_file_raw.close()
