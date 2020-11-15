from django.shortcuts import render,HttpResponse
from .__init__ import model,label
from keras.preprocessing.image import img_to_array
import numpy as np
from PIL import Image
import base64
import io
import cv2
import datetime
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((256, 256))
image_size = 0
directory_root = '../input/plantvillage/'
width=256
height=256
depth=3
# Create your views here.
EPOCHS = 25
INIT_LR = 1e-3
BS = 32
default_image_size = tuple((256, 256))
image_size = 0
width=256
height=256
depth=3
def convert_image_to_array(image_dir):
    try:
        image = cv2.imread(image_dir)
        if image is not None :
            image = cv2.resize(image, default_image_size)   
            return img_to_array(image)
        else :
            return np.array([])
    except Exception as e:
        print(f"Error : {e}")
        return None

def predictions(request):
    if request.method == "GET":
        #print(und)
        return render(request,"app.html")
    image = request.POST["image"]
    img = base64.b64decode(image)
    img_data = Image.open(io.BytesIO(img))
    img_data.resize((256,256))
    name = datetime.datetime
    img_data.save("Image.png")
    val = [convert_image_to_array('Image.png')]
    np_image_list = np.array(val, dtype=np.float16) / 225.0
    pred = model.predict(np_image_list)
    ind = pred.argmax()
    name = label.classes_[ind]
    return HttpResponse("Data REcv Name = "+str(name))
    