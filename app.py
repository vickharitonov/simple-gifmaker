from PIL import Image
from PIL import ImageOps
import os

frames = []
resizing_frames = []
heights = []
widths = []


"""Obtaining images dir"""
gifdir = os.getcwd() + "/" + input('Input your gif catalog: ')


"""Adding image obj to frames list"""
for image in sorted(os.listdir(gifdir)):
    frame = Image.open(f'{gifdir}/{image}')
    frames.append(frame)


"""Obtaining heights from image objects and adding to heights list"""
for obj in frames:
    heights.append(obj.height)


"""Obtaining max height from heights list"""
maxheight = max(heights)


"""Obtaining widths from image objects and adding to widths list"""
for obj in frames:
    widths.append(obj.width)


"""Obtaining max width from widths list"""
maxwidth = max(widths)


"""Obtaining left top right bottom borders for frame object and resizing_frames"""
left = 0
top = 0
right = 0
bottom = 0
for image in frames:
    if image.height < maxheight:
        top, bottom = (maxheight - image.height) / 2



print(heights)
print(widths)
print(maxheight)
print(maxwidth)

"""Saving image file with folling parameters"""
# frames[0].save(
#     'output.gif',
#     save_all=True,
#     append_images=frames[1:],
#     optimize=True,
#     duration=300,
#     loop=0
# )

def makeGif():
    pass


if __name__ == "__main__":
    makeGif()
