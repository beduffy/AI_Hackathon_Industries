from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import sys
import argparse
from collections import Counter
import nltk
from nltk.corpus import stopwords

from transcribe import transcribe_file
from topic_modelling import run_topic_model
import pyteaser_summary
import sentiment

# 2. Audio to text
def audio_to_text(audio_fp, output_fn):
    transcribe_file(audio_fp, output_folder, output_fn)

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
def process_topics(text):
    topics = run_topic_model(text)

    print(topics)

# 3.4 word cloud
def word_cloud(text, output_image_fp):
    s = text
    s_tokens = nltk.word_tokenize(s) #s.split()

    s_tokens = [t for t in s_tokens if not t in stopwords.words('english')]

    print('\nWord Cloud word frequencies:')
    print(Counter(s_tokens).most_common(100))

    import word_cloud
    word_cloud.create_word_cloud(text, output_image_fp)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='Audio file to be recognized')
    args = parser.parse_args()

    global_JSON = {}
    output_folder = 'intermediate_data'
    intermediate_fn = 'Nightfall1.txt'
    intermediate_fn = 'Nightfall_Long.txt'

    #output_folder = 'data/Model_Training'
    #intermediate_fn = '26.txt'
    intermediate_fp = output_folder + '/' + intermediate_fn

    # ------ output_text
    print('Beginning to process audio and converting to text')
    #audio_to_text(args.path, intermediate_fn)
    print('Finished processing audio file')

    audio_text_file_raw = open(intermediate_fp, 'r')
    text_from_file = audio_text_file_raw.read()

    #text_from_file = text_from_file.decode('utf-8')
    #sys.exit()

    print('Beginning to process text file\n')
    # 3.1. # todo find better summariser.
    summarise_text(intermediate_fn, text_from_file)

    # 3.2. # todo find better sentiment model. Run it on parts of text?
    process_sentiment(text_from_file)

    # 3.3. Gone. Forget it.
    #process_topics(text_from_file)

    # 3.4. todo: Able to run for any text.
    word_cloud(text_from_file, 'data/Nightfall.png')

    print('Finished processing text file')
    audio_text_file_raw.close()
