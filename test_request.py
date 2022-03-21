import requests
import json
import base64
from PIL import Image
import utils
import time

def test(img_path):
    # with open(img_path, 'rb') as f:
    #     base64_data = base64.b64encode(f.read())
    #     img = base64_data.decode()
    img_data = Image.open(img_path)
    print(img_data.size)
    img = utils.image_to_base64(img_data)
    
    datas = json.dumps({'base64': img})
    #rec = requests.post("http://127.0.0.1:8000/anime", data=datas) 
    rec = requests.post("http://150.158.96.11:8000/anime", data=datas) 
    print(rec.text)
    new_img = json.loads(rec.text).get('img')

    utils.base64_to_image(new_img,"test_anime.jpg")

def test_deoldify(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img = base64_data.decode()
    datas = json.dumps({'base64': img})
    rec = requests.post("http://150.158.96.11:8000/deoldify", data=datas) 
    new_img = json.loads(rec.text).get('img')

    utils.base64_to_image(new_img,"test_deoldify.jpg")


time_start=time.time()
result= test('4.jpg')

time_end=time.time()
print('totally cost',time_end-time_start)
#result= test('IMG_2341.HEIC')
#result= test_deoldify('2.png')
#result= test_deoldify('IMG_2341.HEIC')
#print(result)
