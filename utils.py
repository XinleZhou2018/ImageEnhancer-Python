import re
import base64
from io import BytesIO
from PIL import Image
from pillow_heif import register_heif_opener



def base64_to_image(base64_str, image_path=None):
    register_heif_opener()
    base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
    byte_data = base64.b64decode(base64_data)
    image_data = BytesIO(byte_data)
    
    img = Image.open(image_data)
    
    if image_path:
        img.save(image_path)
    return img

def image_to_base64(image: Image.Image, fmt='png') -> str:
    output_buffer = BytesIO()
    image.save(output_buffer, format=fmt)
    byte_data = output_buffer.getvalue()
    base64_str = base64.b64encode(byte_data).decode('utf-8')
    return base64_str#f'data:image/{fmt};base64,' + base64_str

