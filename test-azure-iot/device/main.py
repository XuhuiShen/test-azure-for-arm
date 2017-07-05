#! /usr/bin/env python
import os

os.system('python ./iothub_client_sample.py -c "HostName=IOT-nostalgia.azure-devices.cn;DeviceId=sample;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" -p mqtti')

#os.system('python ./iothub_client_sample_class.py -c "HostName=IOT-nostalgia.azure-devices.cn;DeviceId=sample;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" -p mqtti')

#os.system('python ./iothub_client_sample_x509.py -c "HostName=IOT-nostalgia.azure-devices.cn;DeviceId=sample;SharedAccessKey=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" -p mqtti')
