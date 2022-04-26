from PIL import Image, ImageOps, ImageDraw, ImageFont
from StreamDeck.ImageHelpers import PILHelper
from StreamDeck.DeviceManager import DeviceManager
import json
import time
import subprocess
import os


class ConfigNotFound(Exception):
    pass

AssetsPath = './Assets/'
FontPath = './Assets/OpenSans-Bold.ttf'



def initialize_deck():
    deck = DeviceManager().enumerate()[0]
    deck.open()
    deck.reset()
    deck.set_brightness(90)
    print()
    return deck
    

def execute_command(command):
    #Separate command in spaces and put them in a list
    os.system(command)


def key_pressed(deck, key):
    
    
    key_image(deck, key, "", "keyPress.png")
    print("Key command {} ".format(data[str(key)]['command']))
    execute_command(data[str(key)]['command'])
    time.sleep(0.5)
    if data[str(key)]['image'] == "":
        key_image(deck, key, data[str(key)]['text'], "default_key.png")
    else:
        key_image(deck, key, data[str(key)]['text'], data[str(key)]['image'])



    
def load_config(deck):
    try:
        with open('config.json') as json_file:
            global data
            data = json.load(json_file)
    #file not exists
    except FileNotFoundError:
        raise ConfigNotFound("\nConfig not foun\nRead docs for creating a config file\n")
    
    if data is not None and data.keys().__len__() == deck.KEY_COUNT:
        for key in data.keys():
            if data[key]['image'] == "":
                key_image(deck, int(key), data[key]['text'], "default_key.png")
            else:
                key_image(deck, int(key), data[key]['text'], data[key]['image'])

    
    
def key_image(deck, key, text, img):
        image = Image.open(AssetsPath + img)
        image = image.convert('RGB')
        image = PILHelper.create_scaled_image(deck, image, margins=[0, 0, 0, 0])
        
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(FontPath, 15)
        
        draw.text((image.height/2, image.width-7), font=font, text=text, anchor="ms",fill="white")
        
        deck.set_key_image(key, PILHelper.to_native_format(deck, image))