from PIL import Image
import os


# Obtaining images dir
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
COMPRESSED_DIR = BASE_DIR + "/compressed"

# Creating dir for compresed images
if os.path.isdir("compressed"):
    pass
else:
    os.mkdir("compressed")

# input for resources dir
RESOURCES_DIR = None
while True:
    RESOURCES_DIR = BASE_DIR + "/" + input("Select dir with your images: ")
    if os.path.isdir(RESOURCES_DIR):
        RESOURCES_DIR = RESOURCES_DIR
        break
    else:
        print("Wrong catalog name. Try again")

# input for quality number
quality = None
while True:
    quality = input("Choose image quality from 1 to 100 (85 is optimum): ")
    if quality.isdigit() and int(quality) in range(1, 101):
        quality = int(quality)
        break
    else:
        print("Wrong quality size. Try again")

# inout for duration per frame time
duration = None
while True:
    duration = input(
        "Select duration time per frame in milliseconds from 100 to 1000: "
    )
    if duration.isdigit() and int(duration) in range(100, 1001):
        duration = int(duration)
        break
    else:
        print("Wrong duration time. Try again")


class Frames:
    def __init__(self):
        self.frames = []
        self.croppped_frames = []
        self.resized_frames = []
        self.min_width = None
        self.min_width = None

    # Compressing images
    def compression(self):
        for image in os.listdir(RESOURCES_DIR):
            img = Image.open(f"{RESOURCES_DIR}/{image}")
            img.save(f"{BASE_DIR}/compressed/{image}", optimize=True, quality=quality)

    # Finding all images and adding them to frames list
    def collector(self):
        for image in sorted(os.listdir(COMPRESSED_DIR)):
            frame = Image.open(f"{COMPRESSED_DIR}/{image}")
            self.frames.append(frame)

    # Obtaining min height from frames
    def get_minHeight(self):
        heights = []
        for obj in self.frames:
            heights.append(obj.height)
        self.min_height = min(heights)

    # Obtaining min width from frames
    def get_minWidth(self):
        widths = []
        for obj in self.frames:
            widths.append(obj.width)
        self.min_width = min(widths)

    # Cropping frames to min_width x min_height. Due to rounded keys sizes are not the same, then need to resize
    def cropper(self):
        for frame in self.frames:
            if frame.width > self.min_width:
                left = round((frame.width - self.min_width) / 2)
                right = frame.width - left
            else:
                left = 0
                right = self.min_width
            print(left, right)
            if frame.height > self.min_height:
                top = round((frame.height - self.min_height) / 2)
                bottom = frame.height - top
            else:
                top = 0
                bottom = self.min_height
            print(top, bottom)
            with frame as fr:
                fr_crop = fr.crop((left, top, right, bottom))
                self.croppped_frames.append(fr_crop)

    # Resizing frames to min_width x min_height
    def resizer(self):
        for frame in self.croppped_frames:
            with frame as fr:
                resized_frame = fr.resize((self.min_width, self.min_height))
                self.resized_frames.append(resized_frame)

    # Compiling cropped, resized and compressed images into gif
    def compile(self):
        self.resized_frames[0].save(
            "output.gif",
            save_all=True,
            append_images=self.resized_frames[1:],
            optimize=True,
            duration=duration,
            quality=1,
            loop=0,
        )
        # Removing compressed frames
        for image in os.listdir(COMPRESSED_DIR):
            os.remove(f"{COMPRESSED_DIR}/{image}")


def main():
    gif = Frames()
    gif.compression()
    gif.collector()
    gif.get_minHeight()
    gif.get_minWidth()
    gif.cropper()
    gif.resizer()
    gif.compile()


if __name__ == "__main__":
    main()
