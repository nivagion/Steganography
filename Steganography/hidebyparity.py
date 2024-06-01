#LSB!
from PIL import Image #we are hiding the message only in Red pixels, for example if first red pixel is even we look at it as a 0, if its odd its 1...
                      #when we are storing the message, we change value of RED pixels by at most 1, and image looks "almost the same"

def hide_message_in_image(image_path, message):
    img = Image.open(image_path)
    binary_message = ''.join(format(ord(i), '08b') for i in message)
    data_index = 0

    width, height = img.size
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            r, g, b = pixel[:3]  # only take the first three values, we dont use A in RGBA
            if data_index < len(binary_message):
                bit = binary_message[data_index]
                r = r - r % 2 + int(bit)
                img.putpixel((col, row), (r, g, b) + pixel[3:])  # add the remaining values back
                data_index += 1
            else:
                return img

    return img

def retrieve_message_from_image(image_path):
    img = Image.open(image_path)
    binary_message = ""

    width, height = img.size
    for row in range(height):
        for col in range(width):
            pixel = img.getpixel((col, row))
            r = pixel[0]  # only take the red value
            if r % 2 == 0:
                binary_message += '0'
            else:
                binary_message += '1'

    message = ''
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        message += chr(int(byte, 2))
        if message[-5:] == "#####":  # we append '#####' as the end of the message
            break

    return message[:-5]  # remove '#####'
