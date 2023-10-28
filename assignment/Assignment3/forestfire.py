"""
File: forestfire.py
----------------
This program highlights fires in an image by identifying
pixels who red intensity is more than INTENSITY_THRESHOLD times
the average of the red, green, and blue values at a pixel.
Those "sufficiently red" pixels are then highlighted in the
image and the rest of the image is turned grey, by setting the
pixels red, green, and blue values all to be the same average
value.
"""


# The line below imports SimpleImage for use here
# Its depends on the Pillow package being installed
from simpleimage import SimpleImage


# Intensity threshold used to determine is a pixel is
# "sufficiently red" to indicate that it is a fire.
INTENSITY_THRESHOLD = 1.05


def highlight_fires(filename):
    """
    This function should highlight the "red" pixels in the image passed in
    and grayscale all other pixels in the image in order to highlight areas
    of wildfires.

    Input:
        filename (string): name of image file to be read in

    Returns:
        highlighted image with "sufficiently red" pixels highlighted
    """
    image = SimpleImage(filename)
    # Your code to highlight the fires goes here
    for pixel in image:
        # Tìm ngưỡng cường độ của ảnh
        average = (pixel.red + pixel.green + pixel.blue) // 3
        average *= INTENSITY_THRESHOLD
        # Nếu lớn hơn thì đổi sang màu đỏ
        if(pixel.red >= average):
            pixel = set_color(pixel, 255, 0, 0)
        # Nhỏ hơn thì đổi sang đen trắng
        else:
            x = pixel.x
            y = pixel.y
            tmp_pixel = grayscale(pixel)
            image.set_pixel(x, y, tmp_pixel)
    return image

def compute_luminosity (red, green, blue):
    # Sử dụng các trọng số để tính độ sáng của điểm màu
    return (0.299 * red) + (0.587 * green) + (0.114 * blue)


def grayscale(filename):
    pixel = filename
    # set điểm ảnh khi tìm được độ sáng của điểm ảnh
    luminosity = compute_luminosity(pixel.red, pixel.green, pixel.blue)
    pixel = set_color(pixel, luminosity, luminosity, luminosity)
    return pixel

def set_color(filename, red, green, blue):
    pixel = filename
    pixel.red = red
    pixel.green = green
    pixel.blue = blue
    return pixel

def main():
    """
    This program tests your highlight_fires function by displaying
    the original image of a fire as well as the resulting image
    from your highlight_fires function.
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
