#!/usr/bin/env python3
from hue import Hue
import configparser

def help():
    print("Commands:\n\t1. on & off\n\t2. alarm (repeat, red light\
on&off)\n\t3. bri (set the brightness 0-254)\n\t4. colors: orange, red, green, blue & white\n") 
def light(lamp):
    hue = Hue(key ,'192.168.178.25',f'{lamp}')
    help()
    while (command:= input(f'Command(light: {lamp}): ')) != "exit":
        command = command.lower()
        try:
            if command == "on":
                hue.set_lamp(True)
            elif command == "off":
                hue.set_lamp(False)
            elif command == "alarm":
                hue.alarm()
            elif command == "bri":
                hue.set_bri(input("Wich Brigthness? "))
            else:
                hue.set_color(command)
        except:
            print("Invalid command, try again!")

if __name__ == "__main__":
    # Load config and secret API-Key
    config = configparser.ConfigParser()
    config.read('secrets.ini')
    global key 
    key = config['hue']['key']
    while (command:= input("Wich Lamp? ")) != "exit":
        command = command.lower()
        try:
            if command == "büro":
                hue = Hue(key ,'192.168.178.25','7')
            else:
                light(command)
        except:
            print("Invalid command, try again!")
