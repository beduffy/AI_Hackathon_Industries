from azure.storage.blob import ContentSettings
from azure.storage.blob import BlockBlobService

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
