from instacrop import create_cropped_image, max_num_cropped_images

import tkinter as tk
from tkinter import filedialog

class FileBrowserApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Insta Crop!")

        # Entry to display selected file path
        self.file_path_entry = tk.Entry(master, width=40)
        self.file_path_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        # Browse button
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_file)
        self.browse_button.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

        # Display file that has been choosen
        #display photo here after it has been selected

        # Slider (initially hidden)
        self.slider_label = tk.Label(master, text=f"Select a value (1-{max_num_cropped_images('./test-photo.jpg')}):")
        self.slider = tk.Scale(master, from_=1, to=max_num_cropped_images('./test-photo.jpg'), orient=tk.HORIZONTAL)
        self.enter_button = tk.Button(master, text="Enter", command=self.on_enter)

    def browse_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path_entry.delete(0, tk.END)
            self.file_path_entry.insert(0, file_path)

            # Show slider and enter button after file has been chosen
            self.slider_label.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
            self.slider.grid(row=3, column=0, padx=10, pady=10, columnspan=3)
            self.enter_button.grid(row=4, column=0, padx=10, pady=10, columnspan=3)

    def on_enter(self):
        file_path = self.file_path_entry.get()
        slider_value = self.slider.get()

        print("Selected File Path:", file_path)
        print("Slider Value:", slider_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = FileBrowserApp(root)
    root.mainloop()
