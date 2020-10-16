from base64 import b64encode
import urllib.request, cv2
import numpy as np

def encode_image_to_base64string(image_url):
    req = urllib.request.urlopen(image_url)
    image = np.asarray(bytearray(req.read()), dtype=np.uint8)
    image = cv2.imdecode(image, -1)
    resized_image = cv2.resize(image, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_AREA)
    s = b64encode(resized_image.tobytes())
    encoded_string = s.decode("utf-8")
    return encoded_string