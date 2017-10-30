#!/usr/bin/env python

# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Google Cloud Speech API sample application using the REST API for batch
processing.

Example usage:
    python transcribe.py resources/audio.raw
    python transcribe.py gs://cloud-samples-tests/speech/brooklyn.flac
"""

# [START import_libraries]
import argparse
import io
# [END import_libraries]


# [START def_transcribe_file]
def transcribe_file(speech_file, output_fp):
    """Transcribe the given audio file."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_sync_request]
    # [START migration_audio_config_file]
    with io.open(speech_file, 'rb') as audio_file:
        content = audio_file.read()

    audio = types.RecognitionAudio(content=content)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        #sample_rate_hertz=44100,
        language_code='en-US')
    # [END migration_audio_config_file]

    # [START migration_sync_response]
    #
    response = client.recognize(config, audio)
    #operation = client.long_running_recognize(config, audio)

    print('Waiting for operation to complete...')
    #response = operation.result(timeout=90)
    # [END migration_sync_request]
    # Print the first alternative of all the consecutive results.

    output = []


    #file_name_middle_part = speech_file[:-4]
    #file_name_middle_part = 'Nightfall1'

    #output_path = output_folder + '/' + output_fn
    f = open(output_fp, 'w')
    print(response.results)
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))

        output.append(result.alternatives[0].transcript)#
        f.write(result.alternatives[0].transcript)

    f.close()
    print ('Saved text file from audio to path: {}'.format(output_fp))
    #output
    # [END migration_sync_response]
# [END def_transcribe_file]


# [START def_transcribe_gcs]
def transcribe_gcs(gcs_uri):
    """Transcribes the audio file specified by the gcs_uri."""
    from google.cloud import speech
    from google.cloud.speech import enums
    from google.cloud.speech import types
    client = speech.SpeechClient()

    # [START migration_audio_config_gcs]
    audio = types.RecognitionAudio(uri=gcs_uri)
    config = types.RecognitionConfig(
        encoding=enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=16000,
        language_code='en-US')
    # [END migration_audio_config_gcs]

    response = client.recognize(config, audio)
    # Print the first alternative of all the consecutive results.
    for result in response.results:
        print('Transcript: {}'.format(result.alternatives[0].transcript))
# [END def_transcribe_gcs]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'path', help='File or GCS path for audio file to be recognized')
    args = parser.parse_args()
    if args.path.startswith('gs://'):
        transcribe_gcs(args.path)
    else:
        transcribe_file(args.path)
