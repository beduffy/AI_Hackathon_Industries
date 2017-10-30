import time
import sys
import urllib
import base64

from main_api import process

from azure.storage.queue import QueueService

#wav_file_url = 'https://pmovro.blob.core.windows.net/audios/botrecordvoice.wav'
from azure.storage.blob import PublicAccess

'''wav_file_url = 'https://pmovro.blob.core.windows.net/audios/VRO_Update_Recording.wav'
print ('Decoded file name:', wav_file_url)
# https://pmovro.blob.core.windows.net/audios/botrecordvoice.wav

audio_output_path = 'data/' + wav_file_url.split('/')[-1]
a = urllib.urlretrieve (wav_file_url, audio_output_path)'''
#process('data/VRO_Update_Recording_split_less_than_1min.wav')
#sys.exit()

queue_service = QueueService(account_name='pmovroaudioproc84a4', account_key='MWr7H2D76OqO9l7+sHqsVFUc8FbgtoTz4sgpV08L9JW8peK8BRU49mWt8xWZQmOgPP/IFmQTWNI0KAw/hF4e+w==')

while True:
    messages = queue_service.get_messages('pmovro-audio-updated', num_messages=16, visibility_timeout=1)

    '''
        messages = [{'content':'https://pmovro.blob.core.windows.net/audios/botrecordvoice.wav'}]
    print messages[0]['content']
    '''
    if len(messages) > 0:
        print('Found file in Azure Queue')
        for message in messages:
            print(message.content)
            wav_file_url = base64.b64decode(message.content)
            print ('Decoded file name:', wav_file_url)


            # https://pmovro.blob.core.windows.net/audios/botrecordvoice.wav

            audio_output_path = 'data/' + wav_file_url.split('/')[-1]
            a = urllib.urlretrieve (wav_file_url, audio_output_path)
            print ('Wav File Downloaded', a)

            # todo dequeue and save
            # queue_service.delete_message('pmovro-audio-updated', message.id, message.pop_receipt)
            # todo and run main api

            process(audio_output_path)

        break # todo don't have?

    break
    time.sleep(7)
