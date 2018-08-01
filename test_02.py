import tesserocr

from PIL import Image

image=Image.open(r'/home/keller/Downloads/test.jpg')

print(tesserocr.image_to_text(image))