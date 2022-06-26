from channels.generic.websocket import AsyncWebsocketConsumer
from .frec_logic import Facerec
import cv2
import base64
import numpy as np
from .models import *
import json


class VideoConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        await self.accept()
        self.rec = Facerec()

    async def receive(self, text_data): 
        try:
            encoded_data = text_data.split(',')[1]
            data = base64.b64decode(encoded_data)
            np_arr = np.fromstring(data, np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)         
            sample = self.rec.get_frame(img)
            await self.send(json.dumps(sample))     
        except:
            pass       

    async def disconnect(self, close_code):
        pass
