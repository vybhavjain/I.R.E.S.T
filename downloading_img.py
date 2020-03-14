import requests
from bs4 import BeautifulSoup
import os
import tags

def download(search):
    os.chdir(r"C:\Users\VYBHAV JAIN\Desktop\Maistering\new")

    retrieved_keywords = []
    data = ""

    if os.path.isfile('names.txt'):
        with open("names.txt", "r") as f:
            data = f.read()
            retrieved_keywords.append(data)
    else:
        f = open("names.txt", "a")
        f.write(search+"\n")
        f.close()      
    
    retrieved_keywords  = retrieved_keywords[0].split("\n")    
    
    if search in retrieved_keywords :
        return "present"
        
    site = 'https://unsplash.com/s/photos/'+ search
    
    os.mkdir(search)
    os.chdir(os.getcwd()+"\\"+search)
    
    response = requests.get(site)
    soup = BeautifulSoup(response.content,'html.parser')
    #print(soup)
    
    img_tags = soup.find_all('img')
    #print(img_tags)
    
    urls = [img['src'] for img in img_tags]
    urls = list(dict.fromkeys(urls ))
    #print(urls)
    if len(urls) == 3:
        os.chdir(r"C:\Users\VYBHAV JAIN\Desktop\Maistering\new")
        os.rmdir(search) 
        return "invalid"
    
    f = open("names.txt", "a")
    f.write(search+"\n")
    f.close()
    
    for i in range(len(urls)):
        if "photo" in urls[i]:
            r = requests.get(urls[i])
            name =search+str(i)+".jpg" 
            name1 =search+str(i)
            open(name,'wb').write(r.content)
            final_tags = tags.get1_tags(name)
            #os.chdir(os.getcwd()+"\\"+search)
            f = open(name1+".txt", "a")
            for i in range(len(final_tags)):
                f.write(final_tags[i]+"\n")
            f.close()
    storage = os.getcwd()
    #print("Download of the images sucessfull!! It is stored in the folder : ",storage)
    os.chdir('..')
    
    f = open("names.txt", "a")
    f.write(search+"\n")
    f.close()
    
    return storage
