from instacrop import create_cropped_image, max_num_cropped_images

import os
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

def create_image(image_filepath):

    image = Image.open(image_filepath)
    new_height = 200

    aspect_ratio = image.width / image.height
    new_width = int(new_height * aspect_ratio)
    resized_image = image.resize((new_width, new_height))

    return ImageTk.PhotoImage(resized_image)


class FileBrowserApp:

    filepath: str = ''

    def __init__(self, master):
        self.master = master
        self.master.title("Insta Crop!")

        # Entry to display selected file path
        self.file_path_label = tk.Label(master, width=50, text="Select a file to crop:")
        self.file_path_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Browse button
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # Slider (initially hidden)
        self.slider_label_text = tk.StringVar()
        self.slider_label = tk.Label(master, textvariable=self.slider_label_text)
        self.slider = tk.Scale(master, from_=1, to=1, orient=tk.HORIZONTAL)
        self.enter_button = tk.Button(master, text="Enter", command=self.on_enter)

        # Success label (initally hidden)
        self.success_label_text = tk.StringVar()
        self.success_label = tk.Label(master, textvariable=self.success_label_text, wraplength=600)

    def browse_file(self):
        file_path = filedialog.askopenfilename()

        # If there is an image already displayed, remove it not destroy
        if hasattr(self, 'image_canvas'):
            self.image_canvas.destroy()
            if hasattr(self, 'canvas'):
                self.canvas.destroy()
            if hasattr(self, 'success_label'):
                self.success_label_text.set('')

        if file_path:
            self.filepath = file_path

            # Show photo slider and enter button after file has been chosen
            # Display file that has been choosen

            self.image_canvas = tk.Canvas(self.master, width=self.master.winfo_width())
            img = create_image(self.filepath)

            self.label_image = tk.Label(self.image_canvas, image=img)
            self.label_image.image = img
            self.label_image.pack(side=tk.TOP)
            # Position image
            max_cropped = max_num_cropped_images(self.filepath)

            self.image_canvas.grid(row=2, column=0, padx=10, columnspan=3)

            self.slider_label_text.set(f"Select a value (1-{max_cropped}):")
            self.slider_label.grid(row=3, column=0, padx=10, pady=10, columnspan=3)
            self.slider.config(to=max_cropped)
            self.slider.grid(row=4, column=0, padx=10, pady=10, columnspan=3)
            self.enter_button.grid(row=5, column=0, padx=10, pady=10, columnspan=3)

    def on_enter(self):
        saved_folder = create_cropped_image(self.slider.get(), self.filepath)
        self.success_label_text.set(f"Successfully saved in folder: {saved_folder}")

        # Create a canvas element to put the output images on with the width of the tkinter window
        #clear the canvas if it already exists
        if hasattr(self, 'canvas'):
            self.canvas.destroy()
        self.canvas = tk.Canvas(self.master, width=self.master.winfo_width())

        for file in sorted(os.listdir(saved_folder), key=lambda x: int(x.split('-')[0])):
            image = create_image(os.path.join(saved_folder, file))
            self.label_image = tk.Label(self.canvas, image=image)
            self.label_image.image = image
            # Position all the images next to one another and all of them centered in the canvas
            self.label_image.pack(padx=5, pady=15, side=tk.LEFT)

        self.canvas.grid(row=6, column=0, padx=10, pady=10, columnspan=3)

        self.success_label.grid(row=7, column=0, padx=10, pady=10, columnspan=3)

    def crop(self):
        create_cropped_image(self.slider.get(), self.filepath)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileBrowserApp(root)
    root.mainloop()
