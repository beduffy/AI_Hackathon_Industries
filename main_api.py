from __future__ import absolute_import
from __future__ import division, print_function, unicode_literals
import sys
import argparse
from collections import Counter
import json

import nltk
from nltk.corpus import stopwords
from azure.storage.blob import ContentSettings
from azure.storage.blob import BlockBlobService

from transcribe import transcribe_file
from topic_modelling import run_topic_model
import pyteaser_summary
import sentiment


global_JSON = {}


# 2. Audio to text
def audio_to_text(audio_fp, output_fp):
    transcribe_file(audio_fp, output_fp)

# 3.1 Summarisation
def summarise_text(title, text):
    # todo try sumy, smmry,
    summaries = pyteaser_summary.summarise_text(title, text)

    print('\nSummaries:')
    print(summaries)

    # write to global JSON

# 3.2 Sentiment
def process_sentiment(text):
    sentiment_of_text = sentiment.process_sentiment(text)

    print ('\nSentiment:')
    print (sentiment_of_text)
    global_JSON['sentiment'] = sentiment_of_text.classification # todo how positive number.

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

    global_JSON['words'] = [tup[0] for tup in Counter(s_tokens).most_common(5)]

    import word_cloud
    word_cloud.create_word_cloud(text, output_image_fp)

def process(audio_fp):

    output_folder = 'intermediate_data'
    '''intermediate_fn = 'Nightfall1.txt'
    intermediate_fn = 'Nightfall_Long.txt'''

    #output_folder = 'data/Model_Training'
    intermediate_fn = audio_fp.split('/')[-1]
    #intermediate_fp = output_folder + '/' + intermediate_fn
    intermediate_fp = 'intermediate_data/' + intermediate_fn
    # ------ output_text
    print('Beginning to process audio and converting to text')
    audio_to_text(audio_fp, intermediate_fp)
    print('Finished processing audio file')

    audio_text_file_raw = open(intermediate_fp, 'r')
    text_from_file = audio_text_file_raw.read()

    global_JSON['all_text'] = text_from_file
    print ('Text from file:\n\n', text_from_file)
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
    word_cloud(text_from_file, 'images/' + intermediate_fn + '.png')

    print('Finished processing text file')
    audio_text_file_raw.close()

    print('Outputting output JSON')

    '''output_fp = 'intermediate_data/output_file.json'
    with open(output_fp, 'w') as fp:
        json.dump(global_JSON, fp, indent=4)

        block_blob_service = BlockBlobService(account_name='pmovro', account_key='qgwcj0wuewCnFUJMbbGyhQ9IMCZyr64sdaRU7IzYchJBSfl8YCVa3S7yOXgTacNp8RmR+uhB/eobmQ+zgfNbxQ==')

        block_blob_service.create_blob_from_path(
            'outputs',
            output_fp.split('/')[-1],
            output_fp,
            content_settings=ContentSettings(content_type='application/JSON'))

        #'historical_meeting_notes.csv'
        generator = block_blob_service.list_blobs('outputs')
        print('Listing all files in blob outputs:')
        for blob in generator:
            print(blob.name)
        #https://pmovro.blob.core.windows.net/'''

    fd = open('historical_meeting_notes.csv', 'a')
    # 30/10/2017,Data,New sandbox is configured ,Positive
    #
    csv_row = '27/10/2017,Data,' + global_JSON['all_text']  + ',Positive'
    fd.write(csv_row)
    fd.close()

    block_blob_service = BlockBlobService(account_name='pmovro', account_key='qgwcj0wuewCnFUJMbbGyhQ9IMCZyr64sdaRU7IzYchJBSfl8YCVa3S7yOXgTacNp8RmR+uhB/eobmQ+zgfNbxQ==')

    block_blob_service.create_blob_from_path(
                'outputs',
                'historical_meeting_notes.csv',
                'historical_meeting_notes.csv',
                content_settings=ContentSettings(content_type='application/CSV'))

    generator = block_blob_service.list_blobs('outputs')
    print('Listing all files in blob outputs:')
    for blob in generator:
        print(blob.name)

    print('Saved output file to Azure blob')
        #sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'path', help='Audio file to be recognized')
    args = parser.parse_args()

    process(args.path)
