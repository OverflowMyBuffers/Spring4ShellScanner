#coding:utf-8
import re, requests, json
from constants import REGEX, HEADERS

class Swagger:
    def __init__(self, schema):
        self.schema = schema

    def getPaths(self):
        try:
            return self.schema['paths']
        except Exception as e:
            print("Failure to process paths")

def getSchema(url):
    try:
        reg = re.match(REGEX, url)
        res = requests.get(url, headers=HEADERS)
        if res.status_code == 200:
            return reg[1], res.json()
        else:
            raise Exception(f"Application returned a {str(res.status_code)}")
    except Exception as e:
        print(f"Error getting swagger schema: {e}")
        return {}