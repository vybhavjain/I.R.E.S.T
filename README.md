# I.R.E.S.T

Image Retrieval along with Encoded Storage and Tagging

### Using Flask the application performs the following tasks -
1)Exposes a GET request that scrapes images given a keyword.
2)Stores these images locally so that if the keywords repeat, it doesn’t scrape the web again.
3)Using an AI tool it automatically generates descriptive tags for each image. (Imagga API used)
4)Exposes a POST method that takes the byte64 image and its tags and uploads it to a cloud storage (Firebase used)
5)It queries the stored images by a keyword and displays the top 5 relevant images.
