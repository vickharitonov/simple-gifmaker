from PIL import Image
from constants import *
from validators import *


validator = ExtensionValidator(("jpg", "png", "bmp", "jpeg"))


class Compressor:
    def __init__(self, quality):
        self.quality = quality

    # Compressing images
    def compression(self, source_dir):
        imglist = list(filter(validator, os.listdir(source_dir)))
        print(sorted(imglist))
        for image in imglist:
            _ = Image.open(os.path.join(source_dir, image))
            _.save(
                os.path.join(COMPRESSED_DIR, image), optimize=True, quality=self.quality
            )


class Compiler:
    def __init__(self, duration):
        self.duration = duration

    # Compiling into gif
    def compile(self, list):
        list[0].save(
            "output.gif",
            save_all=True,
            append_images=list[1:],
            optimize=True,
            duration=self.duration,
            loop=0,
        )
        # Removing compressed frames
        for image in os.listdir(COMPRESSED_DIR):
            os.remove(f"{COMPRESSED_DIR}/{image}")


class Handler:
    def __init__(self):
        self.frames = []
        self.croppped_frames = []
        self.resized_frames = []
        self.heights = []
        self.widths = []
        self.min_width = None
        self.min_width = None

    # Finding all images and adding them to frames list
    def collector(self, source_dir):
        imglist = list(filter(validator, os.listdir(source_dir)))
        for image in sorted(imglist):
            frame = Image.open(f"{source_dir}/{image}")
            self.frames.append(frame)

    # Obtaining min height from frames
    def get_heights(self):
        for obj in self.frames:
            self.heights.append(obj.height)
        self.min_height = min(self.heights)

    # Obtaining min width from frames
    def get_widths(self):
        for obj in self.frames:
            self.widths.append(obj.width)
        self.min_width = min(self.widths)

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
