#!/usr/bin/env python3
from hue import Hue

def help():
    print("Commands:\n\t1. on & off\n\t2. alarm (repeat, red light\
on&off)\n\t3. bri (set the brightness 0-254)\n\t4. colors: orange, red, green, blue & white\n") 
def light(lamp):
    hue = Hue('AUYosVIdGVuqwefkZ7z8rB4Ni-wh7g84x5KJTFky','192.168.178.25',f'{lamp}')
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
    while (command:= input("Wich Lamp? ")) != "exit":
        try:
            if command == "all":
                print("es")
                for n in range(1, 11):
                    light_[n] = Hue('AUYosVIdGVuqwefkZ7z8rB4Ni-wh7g84x5KJTFky','192.168.178.25',f'{n}')
                    print(n)
            else:
                light(command)
        except:
            print("Invalid command, try again!")
