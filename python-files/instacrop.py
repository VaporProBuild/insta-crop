#instacrop.py

#pixel image on instagram 1080 (length) x 1350 (height) pixels 4:5 ratio

from PIL import Image
import os

class ImageProcessingError(Exception):
    pass

def validate_image_processing(num_images, new_width, img):
    if num_images == 0:
        raise ImageProcessingError("Error! Cannot produce 0 images!")

    if num_images * new_width > img.width:
        raise ImageProcessingError(f"Error! Cannot produce {num_images} images from the original photo.\nMax number of photos is {img.width // new_width}. Reduce the hight to crop more photos in a row.")

def max_num_cropped_images(img_name) -> int:
    try :
        img = Image.open(img_name)
        width = img.height * 4 // 5
        return (img.width // width)
    except:
        return 0

def create_cropped_image(num_images, img_name):

    try:
        img = Image.open(img_name)
        filename = os.path.basename(img.filename)

        new_width = img.height * 4 // 5
        validate_image_processing(num_images, new_width, img)
        new_height = img.height
        middle = img.width / 2
        # Calculate the cropping box first left coordinate
        left = middle - (num_images/2) * new_width # need to do some math to figure this out

        save_folder = f"{img_name.strip(filename)}{filename.split('.')[0]}-cropped"

        # If folder already exists in location then remove the files in it. If it doesn't exist create it.
        if os.path.exists(save_folder):
            for file in os.listdir(save_folder):
                os.remove(os.path.join(save_folder, file))
        else:
            os.mkdir(save_folder)

        for num in range(num_images):
            num+=1

            right = left + new_width
            lower = new_height

            # Crop the image
            cropped_img = img.crop((left, 0, right, lower))
            #cropped_img.show() #testcase to show cropped images
            cropped_img.save(os.path.join(save_folder, f"{num}-{filename}"), quality=100)

            left += new_width
        
        return save_folder

    except ImageProcessingError as e:
        print(f"Error: {e}")
        exit(1)

#create_cropped_image(2, "./test-photo.jpg")