import json
import os

def load_config():
    empty_config ='{"0":{"text":"","image":"","command":""},"1":{"text":"","image":"","command":""},"2":{"text":"","image":"","command":""},"3":{"text":"","image":"","command":""},"4":{"text":"","image":"","command":""},"5":{"text":"","image":"","command":""},"6":{"text":"","image":"","command":""},"7":{"text":"","image":"","command":""},"8":{"text":"","image":"","command":""},"9":{"text":"","image":"","command":""},"10":{"text":"","image":"","command":""},"11":{"text":"","image":"","command":""},"12":{"text":"","image":"","command":""},"13":{"text":"","image":"","command":""},"14":{"text":"","image":"","command":""}}'
    obj = json.loads(empty_config)
   
    try:
        if os.stat('../config.json').st_size == 0:
            with open('../config.json', 'w') as f:
                json.dump(obj, fp=f, indent=4)
        with open('../config.json', 'r') as f:         
            return json.load(f)

    except FileNotFoundError:
        with open('../config.json', 'w') as f:
            json.dump(obj, fp=f, indent=4)
        return obj
       
       
def save_config(config):
    obj = json.dumps(config, indent = 4)
    with open('../config.json', 'w') as f:
        f.write(obj)