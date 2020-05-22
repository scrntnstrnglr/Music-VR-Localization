import os,io
from google.cloud import vision
from google.cloud.vision import types

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'ServiceACToken-InstrumentRec.json'
client = vision.ImageAnnotatorClient()
print(client)

img_uri="https://cdnblog.picsart.com/2015/08/178443533002201.jpg"
image = vision.types.Image()
image.source.image_uri = img_uri
response = client.text_detection(image=image)
print(response)
