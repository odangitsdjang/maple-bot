from interception import *
from game import Game
from player import Player
from map import Map

def bind(context):
    context.set_filter(interception.is_keyboard, interception_filter_key_state.INTERCEPTION_FILTER_KEY_ALL.value)
    print("Click any key on your keyboard.")
    device = None
    while True:
        device = context.wait()
        if interception.is_keyboard(device):
            print(f"Bound to keyboard: {context.get_HWID(device)}.")
            c.set_filter(interception.is_keyboard, 0)
            break
    return device

if __name__ == "__main__":
    # This setup is required for Interception to mimic your keyboard.
    c = interception()      
    d = bind(c)

    # Script for Bowmaster @ SSS1
    g = Game((5, 60, 180, 130))
    p = Player(c, d, g)
    m = Map(p, g)
    # target = (97, 32.5)
    target = (97.5, 48.5)

    m.run_es()
   

        # TODO: Totem Use and equip every 2 hours 
        # TODO: Familiar
        # TODO: Anti bot alert
        # TODO: CC For better flame
        # TODO: class specific stuff
        # TODO: Black mage spawn