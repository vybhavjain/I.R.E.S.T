import requests

#Function to use the imagga API to automatically tag the downloaded image
def get1_tags(image_path):
    
    api_key = "" #Enter API key here
    api_secret = "" #Enter API secret key here

    response = requests.post('https://api.imagga.com/v2/tags',auth=(api_key, api_secret),files={'image': open(image_path, 'rb')})

    ls = []

    for i in range(len(response.json()['result']['tags'])):
        ls.append(response.json()['result']['tags'][i]['tag']['en'])
    tags_list = ls[0:15]
    return tags_list
