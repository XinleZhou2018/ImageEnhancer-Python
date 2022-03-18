import requests
import json
import base64

import utils

def test(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        img = base64_data.decode()
    datas = json.dumps({'base64': img})
    print(datas)
    rec = requests.post("http://127.0.0.1:8000/anime", data=datas) 
    new_img = json.loads(rec.text).get('img')

    utils.base64_to_image(new_img,"test.jpg")
 
result= test('4.jpg')
print(result)
