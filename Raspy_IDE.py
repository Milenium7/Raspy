import tkinter as tk
from tkinter import filedialog

def run_code():
    # Function to run the code in the editor
    code = editor.get("1.0", "end-1c")
    # Add your code interpretation logic here
    # For example, you can call the interpret function from your previous code

def clear_editor():
    # Function to clear the editor
    editor.delete("1.0", "end")

def open_file():
    # Function to open a file and load its content into the editor
    file_path = filedialog.askopenfilename(filetypes=[("Custom Language Files", "*.rpy"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            editor.delete("1.0", "end")
            editor.insert("1.0", content)

def save_file():
    # Function to save the content of the editor to a file
    file_path = filedialog.asksaveasfilename(defaultextension=".rpy", filetypes=[("Custom Language Files", "*.rpy"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            content = editor.get("1.0", "end-1c")
            file.write(content)

# Create main window
root = tk.Tk()
root.title("Custom Language IDE")

# Create text editor
editor = tk.Text(root, wrap="word", width=80, height=25)
editor.pack(fill="both", expand=True)

# Create status bar
status_bar = tk.Label(root, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Create buttons
run_button = tk.Button(root, text="Run", command=run_code)
run_button.pack(side="left", padx=5, pady=5)

clear_button = tk.Button(root, text="Clear", command=clear_editor)
clear_button.pack(side="left", padx=5, pady=5)

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack(side="right", padx=5, pady=5)

save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side="right", padx=5, pady=5)

# Run the Tkinter event loop
root.mainloop()
