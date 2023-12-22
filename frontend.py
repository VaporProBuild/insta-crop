from instacrop import create_cropped_image, max_num_cropped_images

import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

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

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.filepath = file_path

            # Show photo slider and enter button after file has been chosen
            # Display file that has been choosen
            #display photo here after it has been selected
            # Create a photoimage object of the image in the path

            image = ImageTk.PhotoImage(Image.open(self.filepath))
            self.label_image = tk.Label(image=image)
            self.label_image.image = image
            # Position image
            max_cropped = max_num_cropped_images(self.filepath)
            self.label_image.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
            self.slider_label_text.set(f"Select a value (1-{max_cropped}):")
            self.slider_label.grid(row=3, column=0, padx=10, pady=10, columnspan=3)
            self.slider.config(to=max_cropped)
            self.slider.grid(row=4, column=0, padx=10, pady=10, columnspan=3)
            self.enter_button.grid(row=5, column=0, padx=10, pady=10, columnspan=3)

    def on_enter(self):
        print(f"file path: {self.filepath}, slider value: {self.slider.get()}")

    def crop(self):
        create_cropped_image(self.slider.get(), self.filepath)



if __name__ == "__main__":
    root = tk.Tk()
    app = FileBrowserApp(root)
    root.mainloop()
