import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk, ImageDraw

class ImageColorPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Color Picker")
        
        # Initialize images and variables
        self.bmp = None
        self.bmp1 = None
        self.color = None
        self.x, self.y = 0, 0

        # Set up the UI components
        self.picture_box1 = tk.Label(root, borderwidth=2, relief="groove")
        self.picture_box1.grid(row=0, column=0)
        self.picture_box1.bind("<Button-1>", self.on_mouse_down)

        self.picture_box2 = tk.Label(root, borderwidth=2, relief="groove")
        self.picture_box2.grid(row=0, column=1)

        self.color_button = tk.Button(root, text="Apply Color", command=self.apply_color)
        self.color_button.grid(row=1, column=0, columnspan=2, pady=10)

        self.open_image_button = tk.Button(root, text="Open Image", command=self.open_image)
        self.open_image_button.grid(row=2, column=0, columnspan=2, pady=10)

    def open_image(self):
        # Load an image and display in PictureBox1
        file_path = filedialog.askopenfilename()
        if file_path:
            self.bmp = Image.open(file_path)
            self.bmp.thumbnail((300, 300))  # Resize for display purposes
            self.photo = ImageTk.PhotoImage(self.bmp)
            self.picture_box1.config(image=self.photo)

    def on_mouse_down(self, event):
        # Get pixel color at click location in PictureBox1
        if self.bmp:
            self.x, self.y = event.x, event.y
            self.color = self.bmp.getpixel((self.x, self.y))
            self.color_button.config(bg=self.rgb_to_hex(self.color))

    def apply_color(self):
        # Apply selected color to PictureBox2
        if self.bmp:
            self.bmp1 = self.bmp.copy()
            draw = ImageDraw.Draw(self.bmp1)

            # Apply color to specific region (similar to the 100x100 loop in original code)
            for i in range(max(0, self.y - 50), min(self.bmp1.height, self.y + 50)):
                for j in range(max(0, self.x - 50), min(self.bmp1.width, self.x + 50)):
                    if self.bmp.getpixel((j, i)) == self.color:
                        draw.point((j, i), fill=self.color)

            self.photo2 = ImageTk.PhotoImage(self.bmp1)
            self.picture_box2.config(image=self.photo2)

    def rgb_to_hex(self, rgb):
        # Helper function to convert RGB to hex
        return "#{:02x}{:02x}{:02x}".format(*rgb)

root = tk.Tk()
app = ImageColorPicker(root)
root.mainloop()
