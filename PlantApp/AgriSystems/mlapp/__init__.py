print("Hie")
und = "Sample String"
import os
import pickle
print(os.path)
path=os.path.dirname(os.path.abspath(__file__))

model = pickle.load(open(path+"/cnn_model.pkl","rb"))
label = pickle.load(open(path+"/label_transform.pkl","rb"))
