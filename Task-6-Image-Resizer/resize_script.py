from PIL import Image
import os

input_folder = 'input_images'
output_folder = 'output_images'

new_size = (800, 800)
supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp')

if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"Created output folder: {output_folder}")

files = os.listdir(input_folder)

print("Starting image resizing process")
for filename in files:
    if filename.lower().endswith(supported_formats):
        try:
            input_path = os.path.join(input_folder, filename)
            with Image.open(input_path) as img:
                resized_img = img.resize(new_size)
                output_path = os.path.join(output_folder, filename)
                resized_img.save(output_path)
                print(f"Resized and saved: {filename}")

        except Exception as e:
            print(f"Failed to process {filename}: {e}")

print("\n All images have been resized successfully")