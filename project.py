from flask import Flask, redirect, render_template, request, session, url_for
import downloading_img
import decoding_encoding_base64
import retrieve

app = Flask(__name__)

@app.route('/',methods=["GET","POST"])
def main_page():
    if request.method == 'GET':
        return render_template("main_page.html")
    else:
        keyword = request.form['keyword']
        location = downloading_img.download(keyword) # Downloads the images,automatically tags downloaded images(15 tags) and stores it in the folder name --> location
        if location == "present":
            return render_template("main_page.html",keyword = keyword)
        if location == "invalid":
            return render_template("main_page.html",invalidword = keyword)
        decoding_encoding_base64.store(keyword) # Encodes the image in base64 and sends the encoded value + description to the cloud 
        return render_template("keyword.html", keyword=keyword , location = location)

@app.route('/keyword',methods=["GET","POST"])
def keyword():
    if request.method == 'GET':
        return render_template("keyword.html")
    else:
        searchword = request.form['searchword']
        #need to get the image, encode it again , display with tags
        status,a,b = retrieve.search(searchword) # a= image names, b =  descriptions
        length = len(a)
        #image_name = "img2.jpg"
        if status == "fail":
            return render_template("keyword.html", searchword =searchword)
        else:
            return render_template("searchword.html", searchword =searchword ,a=a,b=b ,length=length)
        
if __name__ == '__main__':
	app.run(debug=True,use_reloader=False)
