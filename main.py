import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from ttkthemes import ThemedTk
from PIL import Image

# List of supported image formats
SUPPORTED_FORMATS = ["PNG", "JPEG", "WEBP", "BMP", "GIF", "TIFF"]

# Function to convert image formats
def convert_image(input_path, output_path, output_format):
    try:
        # Open the input image
        with Image.open(input_path) as img:
            # Convert and save in the desired format
            img.save(output_path, format=output_format)
            messagebox.showinfo("Success", f"Image successfully converted to {output_format} format and saved at {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Function to open file dialog for input image
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.webp;*.bmp;*.gif;*.tiff")])
    if file_path:
        input_entry.delete(0, tk.END)  # Clear any previous input
        input_entry.insert(0, file_path)  # Display the selected file path

# Function to select the output format and convert the image
def select_conversion():
    input_file = input_entry.get()
    output_format = output_format_var.get()
    
    if not input_file:
        messagebox.showwarning("Input Error", "Please select an input image.")
        return
    
    # Define output path
    output_path = filedialog.asksaveasfilename(defaultextension=f".{output_format.lower()}", filetypes=[(f"{output_format} files", f"*.{output_format.lower()}")])
    if not output_path:
        return  # User cancelled saving
    
    # Perform the conversion
    convert_image(input_file, output_path, output_format)

# Create the main window using a modern theme
root = ThemedTk(theme="arc")
root.title("Image Format Converter")
root.geometry("400x300")
root.resizable(False, False)

# Create a frame for the content
frame = ttk.Frame(root, padding=20)
frame.pack(fill="both", expand=True)

# Create a label for input image selection
input_label = ttk.Label(frame, text="Select Input Image:")
input_label.pack(fill="x", pady=5)

# Create an entry box for input image path
input_entry = ttk.Entry(frame, width=40, font=("Arial", 12))
input_entry.pack(fill="x", pady=10)

# Create a button to open file dialog for input image
input_button = ttk.Button(frame, text="Browse", command=open_file)
input_button.pack(pady=5)

# Create a label for output format selection
output_label = ttk.Label(frame, text="Select Output Format:")
output_label.pack(fill="x", pady=5)

# Create a dropdown (combobox) for output format selection
output_format_var = tk.StringVar()
output_combobox = ttk.Combobox(frame, textvariable=output_format_var, values=SUPPORTED_FORMATS, state="readonly", font=("Arial", 12))
output_combobox.set("PNG")  # Default selection
output_combobox.pack(fill="x", pady=10)

# Create a button to trigger the conversion
convert_button = ttk.Button(frame, text="Convert", command=select_conversion)
convert_button.pack(pady=20)

# Run the main loop
root.mainloop()
