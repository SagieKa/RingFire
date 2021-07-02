from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
import cv2
from PIL import Image
from sendMessage import sendMessage
from urlMap import getMAp
fire = 'https://instaface.co.il/wp-content/uploads/2020/03/%D7%9C%D7%94%D7%A4%D7%95%D7%9A-%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9C%D7%A6%D7%99%D7%95%D7%A8-7-1.png'
key = "7b26cb22cdf14b07b35af19d57471f5f"
endpoint = "https://sagiekadomain.cognitiveservices.azure.com/"


def config(img):
    print(img)
    fire = 'https://instaface.co.il/wp-content/uploads/2020/03/%D7%9C%D7%94%D7%A4%D7%95%D7%9A-%D7%AA%D7%9E%D7%95%D7%A0%D7%94-%D7%9C%D7%A6%D7%99%D7%95%D7%A8-7-1.png'
    # network to api of Microsoft
    client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
    # collect all refrens of image
    des = client.describe_image(img)
    print('the des:', des)
    return des


fire_text = ''
percent = ''


def reconigze_fire(img, adressF):
    adress = adressF

    print("statring reconigze_fire func..................")
    print(img)

    des = config(img)
    print(des)
    # reconigze the fire image
    for caption in des.captions:
        # get image of description the image
        fire_text = caption.text
        # percent of fire image
        percent = caption.confidence

        if 'fire' in fire_text:
            print('true')
            mapLocation = getMAp(adress)
            sendMessage(fire_text+' '+str(percent),
                        ' the loaction: ' + mapLocation)
            return fire_text+' '+str(percent)
        else:
            print('false')
            return 'you are liar!!!'
