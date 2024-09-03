import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, ttk
import imageio
import os
import datetime

def select_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        folder_label.config(text=f"Selected Folder: {folder_path}")
        start_button.config(state=tk.NORMAL)
        global selected_folder
        selected_folder = folder_path

def convert_files():
    if not selected_folder:
        messagebox.showerror("Error", "No folder selected!")
        return

    # Create a new folder for the converted images
    new_folder_path = os.path.join(selected_folder, "Converted_Images")
    os.makedirs(new_folder_path, exist_ok=True)

    source_format = source_combobox.get().lower()
    target_format = target_combobox.get().lower()

    files = [f for f in os.listdir(selected_folder) if f.lower().endswith(source_format)]
    total_files = len(files)

    for index, filename in enumerate(files):
        try:
            image = imageio.imread(os.path.join(selected_folder, filename))
            new_filename = f"converted_image_{index + 1}_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.{target_format}"
            imageio.imwrite(os.path.join(new_folder_path, new_filename), image)
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            feedback_text.insert(tk.END, f"[{timestamp}] Converted {filename} to {new_filename} successfully.\n")
        except Exception as e:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            feedback_text.insert(tk.END, f"[{timestamp}] Error converting {filename}: {e}\n")

        # Update progress bar and percentage label
        progress = int((index + 1) / total_files * 100)
        progress_bar['value'] = progress
        progress_label.config(text=f"{progress}%")
        root.update_idletasks()

    # Reset progress bar and label
    progress_bar['value'] = 0
    progress_label.config(text="0%")
    messagebox.showinfo("Done", "All conversions completed successfully!")

# Create the main window
root = tk.Tk()
root.title("File Converter")

# Create a button to select the folder
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=10)

# Label to display the selected folder
folder_label = tk.Label(root, text="No folder selected")
folder_label.pack(pady=5)

# Create labels and comboboxes for source and target formats
source_label = tk.Label(root, text="Select Source Format:")
source_label.pack(pady=5)
source_combobox = ttk.Combobox(root, values=['.heic', '.heif', '.jpg', '.png'])
source_combobox.set('.heic')
source_combobox.pack(pady=5)

target_label = tk.Label(root, text="Select Target Format:")
target_label.pack(pady=5)
target_combobox = ttk.Combobox(root, values=['.jpg', '.png', '.heic', '.heif'])
target_combobox.set('.jpg')
target_combobox.pack(pady=5)

# Create a button to start the conversion
start_button = tk.Button(root, text="Start Conversion", command=convert_files, state=tk.DISABLED)
start_button.pack(pady=10)

# Create a scrolled text widget to display feedback
feedback_text = scrolledtext.ScrolledText(root, height=10, width=50)
feedback_text.pack(pady=10)

# Create a progress bar
progress_bar = ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.pack(pady=10)

# Create a label to display the progress percentage
progress_label = tk.Label(root, text="0%")
progress_label.pack(pady=10)

# Run the application
root.mainloop()
