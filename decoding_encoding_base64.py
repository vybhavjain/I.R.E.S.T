import base64
import os
from firebase import firebase

#Connects to the firebase storage
firebase = firebase.FirebaseApplication('', None) ##url to the firebase database


#Encodes to base 64
base_value = ""
def encode(img_path):
    with open(img_path,"rb") as img_file:
        base64_value = base64.b64encode(img_file.read())
        #print(base64_value)
        return base64_value.decode('utf-8')

#Decodes base 64 code
def decode(base64_value,name):
    with open(name + ".jpg", "wb") as fh:
        fh.write(base64.b64decode(base64_value))

#Function to store the image to the cloud        
def store(search):
    os.chdir(r"C:\Users\VYBHAV JAIN\Desktop\Maistering\new\\" + search)
    entries = os.listdir(os.getcwd())
    text_names = []
    images_names= []
    for i in range(len(entries)):
        if ".txt" in entries[i]:
            text_names.append(entries[i])
    for i in range(len(entries)):
        if ".jpg" in entries[i]:
            images_names.append(entries[i])
            
    for i in range(len(images_names)):
        a = {}
        f = open(text_names[i], "r")
        description = f.read()
        a['description'] = description
        a['base64'] = encode(images_names[i])
        var_x = images_names[i]
        name_to_save = var_x[:-4]
        result1 = firebase.post(search + "/" + name_to_save + "/" , data = a)
