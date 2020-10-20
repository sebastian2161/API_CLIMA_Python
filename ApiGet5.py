import requests
import json
import sys


def Ciudad_JSON(ciudad):


    url = "http://api.openweathermap.org/data/2.5/weather?q="
    
    key_api = "&APPID=08815a58bb814346d563c542c3103380"

    url_v1 = url + ciudad + key_api

    print (url_v1)

    response = requests.get(url_v1, params=0)
    print(response)

    if response.status_code == 200:
       payload = response.json()
       results=payload.get('main',[])
       print(results)


if __name__ == "__main__":

   Ciudad_JSON(sys.args[1])    