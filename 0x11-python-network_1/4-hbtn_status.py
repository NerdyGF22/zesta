#!/usr/bin/python3
"""
- script that fetches https://alx-intranet.hbtn.io/status
- displays the body of the response 
- decoded in utf-8

"""
import requests


def main():
   req = requests.get("https://intranet.hbtn.io/status")
   print("Body response:")
   print("\t- type: {}".format(type(req.text)))
   print("\t- content: {}".format(req.text))


if "__name__" == "__main__":
    main()
