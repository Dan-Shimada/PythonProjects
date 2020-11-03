import requests
from io import BytesIO
from PIL import Image

r = requests.get("https://super.abril.com.br/wp-content/uploads/2014/09/espaco.jpg")
print("Status code: ", r.status_code)

image = Image.open(BytesIO(r.content))

print(image.size, image.format, image.mode)
path = "./image.jpg"
try:
    image.save(path, image.format)
except IOError:
    print("Cannot save image")
