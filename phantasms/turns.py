from PIL import Image
from pytesseract import image_to_string
from config import screenshot_path


def get_turns():
    img = Image.open(screenshot_path)
    img_size = img.size

    gap = (img_size[0] - 1920) / 2
    left = gap + 1280
    right = left + 100
    bottom = img_size[1] / 20

    region = img.crop((left, 0, right, bottom))
    text = image_to_string(region, config='--psm 7 -c tessedit_char_whitelist=/1234')
    print(text)

    return text
