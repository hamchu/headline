from base64 import b64encode
import urllib.request, cv2
import numpy as np

def encode_image_to_base64string(image_url):
    req = urllib.request.urlopen(image_url)
    image = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    resized_image = cv2.resize(image, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    encoded_string = b64encode(cv2.imencode('.jpg', resized_image)[1]).decode("utf-8")
    return encoded_string