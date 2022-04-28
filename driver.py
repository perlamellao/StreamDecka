from deck_utils import *
import threading
import time
from config_editor.main import main as main_config_editor


def daemon(deck):
    while True:
        for key in range(deck.KEY_COUNT):
            if deck.key_states()[key]:
                t2 = threading.Thread(target=key_pressed, args=(deck, key))
                t2.start()
        time.sleep(0.2)
            
        
        
def gui(deck):
    main_config_editor(deck)
    



if __name__ == "__main__":
    
    try:
        deck = initialize_deck()
        load_config(deck)
        
        t1 = threading.Thread(target=daemon, args=(deck,))
        t1.start()
        gui(deck)
        
    except KeyboardInterrupt:    
        print("\n\nKeyboardInterrupt detected. Exiting.")
        t1.join()              
        deck.reset()
        deck.close()
    except ConfigNotFound as e:
        print(e)
        t1.join()
        deck.reset()
        deck.close()   
        
        