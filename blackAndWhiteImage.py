from PIL import Image
import matplotlib.pyplot as plt

def black_and_white_dithering(input_image_path, output_image_path, dithering=False):
    color_image = Image.open('image.jpg')
    if dithering:
        bw = color_image.convert('1')
    else:
        bw = color_image.convert('1', dither=Image.NONE)
    bw.save(output_image_path)

if __name__ == '__main__':
    black_and_white_dithering('image.jpg', 'sample3.jpg')




