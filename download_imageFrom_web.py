import random
import urllib.request

def download_img(url):
    name= random.randrange(1,1000)
    full_name= str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)

download_img("https://cdn.pixabay.com/photo/2013/11/26/14/36/japan-218615_960_720.jpg")