#NOTE:  This must be the first call in order to work properly!
from deoldify import device
from deoldify.device_id import DeviceId
#choices:  CPU, GPU0...GPU7
device.set(device=DeviceId.GPU0)



import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'

import torch

if not torch.cuda.is_available():
    print('GPU not available.')
    
import fastai
from deoldify.visualize import *
import warnings
warnings.filterwarnings("ignore", category=UserWarning, message=".*?Your .*? set is empty.*?")

colorizer = get_image_colorizer(artistic=True)

#colorizer.plot_transformed_image("test_images/2.png", render_factor=10, compare=True)

img = colorizer.get_transformed_image(
            "2.png", render_factor=10, post_process=True, watermarked=False
        )
img.save("2_new.png")