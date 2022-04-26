from deck_utils import *
import threading

import time



def main(deck):

    while True:
        for key in range(deck.KEY_COUNT):
            if deck.key_states()[key]:
                t1 = threading.Thread(target=key_pressed, args=(deck, key))
                t1.start()
        time.sleep(0.2)      


if __name__ == "__main__":
    
    try:
        deck = initialize_deck()
        load_config(deck)

        main(deck)  
    except KeyboardInterrupt:    
        print("\n\nKeyboardInterrupt detected. Exiting.")                  
        deck.reset()
        deck.close()
    except ConfigNotFound as e:
        print(e)
        deck.reset()
        deck.close()   
        
        