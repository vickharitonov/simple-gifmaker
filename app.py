from PIL import Image
from PIL import ImageOps
import os


"""Obtaining images dir"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESOURCES_DIR = BASE_DIR + "/" + input("Choose your gif catalog: ")


class Frames:
    def __init__(self):
        self.frames = []
        self.croppped_frames = []
        self.resized_frames = []
        self.min_width = None
        self.min_width = None


    def collector(self):
        for image in sorted(os.listdir(RESOURCES_DIR)):
            frame = Image.open(f"{RESOURCES_DIR}/{image}")
            self.frames.append(frame)

    def get_minHeight(self):
        heights = []
        for obj in self.frames:
            heights.append(obj.height)
        self.min_height = min(heights)

    def get_minWidth(self):
        widths = []
        for obj in self.frames:
            widths.append(obj.width)
        self.min_width = min(widths)

    def cropper(self):
        for frame in self.frames:
            if frame.width > self.min_width:
                left = round((frame.width - self.min_width) / 2)
                right = frame.width-left
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

    def resizer(self):
        for frame in self.croppped_frames:
            with frame as fr:
                resized_frame = fr.resize((self.min_width, self.min_height))
                self.resized_frames.append(resized_frame)
                
    
    def compile(self):
        self.croppped_frames[0].save(
        'output.gif',
        save_all=True,
        append_images=self.croppped_frames[1:],
        optimize=True,
        duration=600,
        loop = 0
        )

test = Frames()
test.collector()
test.get_minHeight()
test.get_minWidth()
test.cropper()
test.resizer()
test.compile()
print(test.min_height)
print(test.min_width)
print(test.croppped_frames)
print(test.resized_frames)
print(len(test.resized_frames))

# if __name__ == "__main__":
