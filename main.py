#main.py

#pixel image on instagram 1080 (length) x 1350 (height) pixels 4:5 ratio

from PIL import Image

num_images = 1

img = Image.open("./test-photo.jpg")
img.show()
print(img.size)

new_width = img.height * 4 // 5
print("new width = ", new_width)
new_height = img.height

# Calculate the cropping box
left = (img.width - new_width) // 2 # need to do some math to figure this out
upper = 0
right = left + new_width
lower = new_height

# Crop the image
cropped_img = img.crop((left, upper, right, lower))
cropped_img.show()
print(cropped_img.size)

# Trival solution to make the image into 2 images from left to right

print("success")
