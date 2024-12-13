from PIL import Image
import tkinter as tk

# Create a solid color image (e.g., 480x320 with a default color)
width, height = 480, 320
image = Image.new("RGB", (width, height), color="blue")  # Initial color: blue

# Modify the image color (e.g., changing it to red)
pixels = image.load()  # Access the image pixels
for i in range(width):
    for j in range(height):
        pixels[i, j] = (255, 0, 0)  # Change all pixels to red

# Create a Tkinter window
root = tk.Tk()

# Convert the PIL image to Tkinter-compatible PhotoImage
photo = tk.PhotoImage(master=root, width=width, height=height)
photo.put(image.tobytes())  # Convert the PIL image to a byte stream for Tkinter

# Display the image in a Tkinter Label
label = tk.Label(root, image=photo)
label.pack()

# Run the Tkinter event loop
root.mainloop()

