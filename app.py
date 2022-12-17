import os
from constants import *
from image_handlers import *

# Setting up images quality
quality = None
while True:
    try:
        quality = int(input("Enter image quality from 1 to 100 (85 is recommended): "))
    except ValueError:
        print("Please enter a valid integer 1-100")
        continue
    if quality in range(1, 101):
        print(f"You've entered quality: {quality}")
        break
    else:
        print("Quality must be in range 1-100")

# Setting up duration
duration = None
while True:
    try:
        duration = int(
            input("Enter duratin time per frame in milliseconds 100-1000: ")
        )
    except ValueError:
        print("Please enter a valid integer 100-1000")
        continue
    if duration in range(100, 1001):
        print(f"You've entered duration: {duration} ms per frame")
        break
    else:
        print("Duration must be in range 100-1000")

# Setting up RESOURCES_DIR
RESOURCES_DIR = None
while True:
    RESOURCES_DIR = os.path.join(BASE_DIR, input("Select dir with your images: "))
    if os.path.isdir(RESOURCES_DIR):
        RESOURCES_DIR = RESOURCES_DIR
        print(f"You've selected {RESOURCES_DIR} as source directory")
        break
    else:
        print("Such a directory doesn't exist. Please try again")

# Renaming all files in resource dir to lowercase
for file in os.listdir(RESOURCES_DIR):
    os.rename(
        os.path.join(RESOURCES_DIR, file), os.path.join(RESOURCES_DIR, file.lower())
    )

# Creating a directory for compressed images
if os.path.isdir("compressed"):
    pass
else:
    os.mkdir("compressed")

handler = Handler()
compressor = Compressor(quality)
compiler = Compiler(duration)

# run sequence for main 
def run(resource):
    handler.collector(resource)
    handler.get_heights()
    handler.get_widths()
    # if all images are the same size -> compile
    if len(set(handler.heights)) == 1 and len(set(handler.widths)) == 1:
        compiler.compile(handler.frames)
    # if images are not the same size, they'll be cropped and resized -> compile
    else:
        handler.cropper()
        handler.resizer()
        compiler.compile(handler.resized_frames)


def main():
    if quality != 100:
        compressor.compression(RESOURCES_DIR)
        run(COMPRESSED_DIR)
    else:
        run(RESOURCES_DIR)


if __name__ == "__main__":
    main()
