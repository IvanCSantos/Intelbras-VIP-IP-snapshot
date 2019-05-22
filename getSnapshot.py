import requests
from PIL import Image
from io import BytesIO
import time

# API endpoint
URL = ""

# Path and filename
path = ""
filename = time.strftime("%Y%m%d%H%M")
extension = ".jpg"

# Request
r = requests.get(url = URL)

# Image data
img = Image.open(BytesIO(r.content))

# Image file
img.save(path + "/" + filename + extension)