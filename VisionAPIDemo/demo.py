import os,io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'leafy-acumen-268610-a38fd0012f87.json'
client = vision.ImageAnnotatorClient()

print(client)