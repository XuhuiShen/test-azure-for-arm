#! /usr/bin/env python

from azure.storage.file import FileService
from azure.storage.file import ContentSettings

file_service = FileService(account_name='nostalgia', account_key='HGEt9nDGre2nKZMnHxjtUrvHr/gCFSeJty/l5gLq1DmA2QGvSjK56jBBbfgFnPjLVRxS5Hou5RzcUttmuRIKmg==', endpoint_suffix='core.chinacloudapi.cn')

file_service.create_directory('memoryshare', 'memorydir')

file_service.create_file_from_path(
    'memoryshare',
    'memorydir',
    'memoryfile',
    'sunset.png',
    content_settings=ContentSettings(content_type='image/png'))

generator = file_service.list_directories_and_files('memoryshare')
for file_or_dir in generator:
    print(file_or_dir.name)

file_service.get_file_to_path('memoryshare', 'memorydir', 'memoryfile', 'out-sunset.png')
file_service.delete_file('memoryshare', 'memorydir', 'memoryfile')
