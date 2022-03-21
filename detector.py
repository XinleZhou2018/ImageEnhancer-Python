import os


from PIL import Image
import numpy as np

import torch
from torchvision.transforms.functional import to_tensor, to_pil_image

from model import Generator

from deoldify.visualize import get_image_colorizer

check_point = './weights/face_paint_512_v2.pt' #face_paint_512_v1.pt

def detect_anime(img):
    print(img.size)
    net = Generator()
    net.load_state_dict(torch.load(check_point, map_location="cpu"))
    net.eval()
    img = img.convert("RGB")
    with torch.no_grad():
        img = to_tensor(img).unsqueeze(0) * 2 - 1
        out = net(img, False).cpu()
        out = out.squeeze(0).clip(-1, 1) * 0.5 + 0.5
        out = to_pil_image(out)
    return out

def detect_deoldify(img):

    colorizer = get_image_colorizer(artistic=True)
    new_img = colorizer.get_transformed_image_new(
            img, render_factor=10, post_process=True, watermarked=False
        )
    return new_img
