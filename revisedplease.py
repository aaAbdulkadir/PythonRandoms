from PIL import Image
import matplotlib.pyplot as plt
from pylab import *

def black_and_white_dithering(input_image_path, output_image_path, dithering=False):
    color_image = Image.open('image.jpg')
    if dithering:
        bw = color_image.convert('1')
    else:
        bw = color_image.convert('1', dither=Image.NONE)

    # Crop image to get rid of background interruptions
    cropped = bw.crop((400, 0, 800, 600))

    cropped.save(output_image_path)

if __name__ == '__main__':
    black_and_white_dithering('image.jpg', 'sample4.jpg')
