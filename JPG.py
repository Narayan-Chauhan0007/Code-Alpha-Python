import os
import shutil

# Source and destination folders (change paths as needed)
source_folder = r"C:\Users\YourName\Pictures\SourceFolder"
destination_folder = r"C:\Users\YourName\Pictures\JPG_Files"

# Create destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Move .jpg files
for filename in os.listdir(source_folder):
    if filename.lower().endswith(".jpg"):
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename}")

print("✅ All .jpg files moved.")
