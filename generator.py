import pyqrcode
import png
from pyqrcode import QRCode
import random
import string

def generate(url):
    image = pyqrcode.create(url)
    randomName = get_random_string(20)
    image.png(randomName, scale=8)
    return randomName



def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str+'.png'
   

