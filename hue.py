#!/usr/bin/env python3

import requests
from time import sleep

class Hue:
    def __init__(self, user, ip, lamp):
        self.user = user
        self.ip = ip
        self.lamp = lamp
        self.url = f'http://{self.ip}/api/{self.user}/lights/{self.lamp}/state/'

    def set_lamp(self, is_on):
        data = {'on' : is_on}
        requests.put(self.url, json=data)

    def set_color(self, color):
        if color == "orange":
            data = {"on" : True, "sat": 254, "bri" : 254, "hue" : 10880}
        elif color == "green":
            data = {"on" : True, "sat": 254, "bri" : 254, "hue" : 21760}
        elif color == "white":
            data = {"on" : True, "sat": 254, "bri" : 254, "hue" : 32640}
        elif color == "blue":
            data = {"on" : True, "sat": 254, "bri" : 254, "hue" : 43520}
        elif color == "red":
            data = {"on" : True, "sat": 254, "bri" : 254, "hue" : 65280}
        requests.put(self.url, json=data)
    
    def set_bri(self, bri):
        data = {"on" : True, "bri" : int(f'{bri}')}
        requests.put(self.url, json=data)

    def alarm(self):
            x = 0
            self.set_color("red")
            while x < 5:
                self.set_lamp(False)
                sleep(2)
                self.set_lamp(True)
                sleep(2)
                x += 1
            self.set_color("green")
