# -*- coding: utf-8 -*-
import requests
import sys

def main():
    url = "https://notify-api.line.me/api/notify"
    token = 'V85JN8u6CsvnF6AMDnFOWGdDa0J9zMEXdb0NVcmCwBE'
    headers = {"Authorization" : "Bearer "+ token}

    args = sys.argv
    if args[1]:
        message =  '通常終了'
    else :
        message = '異常終了'
    payload = {"message" :  message}
    #files = {"imageFile": open("end.jpg", "rb")}

    #r = requests.post(url ,headers = headers ,params=payload, files=files)
    r = requests.post(url ,headers = headers ,params=payload)

if __name__ == '__main__':
    main()
