#main.py

#pixel image on instagram 1080 (length) x 1350 (height) pixels

from PIL import Image

img = Image.open("./test-photo.jpg")
img.show()
img = img.resize((1080, 1350))
img.show()
print(img.size)


print("success")
