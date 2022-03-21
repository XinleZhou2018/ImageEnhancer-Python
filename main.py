from fastapi import FastAPI
from pydantic import BaseModel
import json
import utils
from detector import detect_anime, detect_deoldify
from urllib.parse import unquote

app = FastAPI()


class Item(BaseModel):
    base64: str = None  #图片base64

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/anime")
async def anime(request_data: Item):
    base64_data = request_data.base64
    base64_data = unquote(base64_data, 'utf-8')
    img = utils.base64_to_image(base64_data)
    new_img = detect_anime(img)
    img_data = utils.image_to_base64(new_img)
    return {"message": "success","img":img_data}


@app.post("/deoldify")
async def anime(request_data: Item):
    base64_data = request_data.base64
    base64_data = unquote(base64_data, 'utf-8')
    img = utils.base64_to_image(base64_data)
    new_img = detect_deoldify(img)
    img_data = utils.image_to_base64(new_img)
    return {"message": "success","img":img_data}

