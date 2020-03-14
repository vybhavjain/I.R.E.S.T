from firebase import firebase
import decoding_encoding_base64
import os

firebase = firebase.FirebaseApplication('', None) #Firebase database url here

# Function that takes in the keyword and retrives the base64 value along with the descriptions from firebase!
def search(searchword):
    status = ""
    none = []
    result = firebase.get('/', None)
    present_keys = list(result.keys())
    if searchword not in present_keys:
        status= "fail"
        return status,none,none
    else:
        overall_base64 = []
        overall_description = []
        overall_locations = []
        #searchword = "pencil"
        result = firebase.get('/'+ searchword,None)
        present_images= list(result.keys())
        
        for i in range(len(present_images)):
            result = firebase.get('/'+ searchword+ '/' + present_images[i],None) 
            default_name= list(result.keys())
            base64 = firebase.get('/'+ searchword+ '/' + present_images[i]+'/' + default_name[0] +'/base64',None)
            description =firebase.get('/'+ searchword+ '/' + present_images[i]+'/' + default_name[0] +'/description',None) 
            overall_base64.append(base64)
            overall_description.append(description)
        
        os.chdir(r"C:\Users\VYBHAV JAIN\Desktop\Maistering\static")

        for i in range(len(overall_base64)):
            decoding_encoding_base64.decode(overall_base64[i],present_images[i])
            f = open(present_images[i]+".txt", "w")
            f.write(overall_description[i])
            f.close()
            overall_locations.append(os.getcwd()+"\\"+present_images[i] + ".jpg" )
        os.chdir('..')
        for i in range(len(present_images)):
            present_images[i] = present_images[i] + ".jpg" 
        status = "success"
        return status,present_images,overall_description
