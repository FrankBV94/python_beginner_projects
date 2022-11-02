# install pillow
# import pillow
# open up the image we want to resize usin python
# print the current size of the image
# specify the size we wanna change it to
# save the new resized image

from PIL import Image

image = Image.open('image.jpg')

print(f"Current size: {image.size}")
