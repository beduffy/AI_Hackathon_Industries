

block_blob_service.create_blob_from_path(
            'audios',
            'VRO_Update_Recording.wav',
            'data/VRO_Update_Recording.wav',
            content_settings=ContentSettings(content_type='application/wav'))

generator = block_blob_service.list_blobs('audios')
print('Listing all files in blob outputs:')
for blob in generator:
    print(blob.name)
