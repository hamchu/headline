from base64 import b64encode
import urllib.request, cv2
import numpy as np

def encode_image_to_base64string(image_url):
    with urllib.request.urlopen(image_url) as image_file:
        s = b64encode(image_file.read())
        encoded_string = s.decode("utf-8")
    return encoded_string