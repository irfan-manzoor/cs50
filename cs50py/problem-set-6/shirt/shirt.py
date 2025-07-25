from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) != 3:
        sys.exit("Usage: python shirt.py <input_image> <output_image>")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    if not is_valid_extension(input_path) or not is_valid_extension(output_path):
        sys.exit("Invalid input or output format")

    if not have_same_extension(input_path, output_path):
        sys.exit("Input and output have different extensions")

    edit_photo(input_path, output_path)

def is_valid_extension(file_path):
    valid_extensions = {'.jpg', '.jpeg', '.png'}
    return os.path.splitext(file_path)[1].lower() in valid_extensions

def have_same_extension(input_path, output_path):
    return os.path.splitext(input_path)[1].lower() == os.path.splitext(output_path)[1].lower()

def edit_photo(input_path, output_path):
    try:
        shirt = Image.open("shirt.png")
        with Image.open(input_path) as input_image:
            input_cropped = ImageOps.fit(input_image, shirt.size)
            input_cropped.paste(shirt, mask=shirt)
            input_cropped.save(output_path)
        print("Image processing completed successfully")
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
