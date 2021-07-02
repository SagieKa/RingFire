from flask import Flask, request, jsonify
from reconigzeFire import reconigze_fire
from downloadPic import download
import json
app = Flask(__name__)

# open server with flask api


@app.route("/", methods=['POST'])
def home():
    url = ''
    # get url image from BotFire
    data = request.stream.read()
    # print(data)
    objectData = json.loads(data)
    adress = objectData["adress"]
    urlImage = objectData["url"]

    # return "hi"
    # convert url to string
    # for i in urlI
    # mage.text:
    #     url += chr(i)
    # print(str(url))

    # Download image from bot to server
    return download(urlImage, adress)


if __name__ == "__main__":
    app.run()
