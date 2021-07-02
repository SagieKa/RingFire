import requests
from upload_File_Firebase import getUrl


def download(url, adressF):
    adress = adressF

    print("statring downloadPic func.........")
    # open image on the server
    f = open('fire.jpg', 'wb')
    # download the image from url
    f.write(requests.get(url).content)
    # close the file
    f.close()
    # call to getUrl function
    # print(adress)
    return getUrl(adress)
