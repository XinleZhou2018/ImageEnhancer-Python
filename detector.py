import os


from PIL import Image
import numpy as np

import torch
from torchvision.transforms.functional import to_tensor, to_pil_image

from model import Generator

check_point = './weights/face_paint_512_v2.pt' #face_paint_512_v1.pt

def detect(img):
    new_img = None
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
