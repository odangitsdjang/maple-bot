from interception import *
from game import Game
from classes.bow_master import BowMaster

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

    # Define buff keys
    BUFF_90 = ("Q", "W", "1")
    BUFF_120 = ("2", "3", "6")

    # Script for Bowmaster @ SSS1
    g = Game((5, 60, 180, 130))
    # p = Player(c, d, g)
    p = BowMaster(c,d,g, BUFF_90, BUFF_120)

    p.run_es()
   

        # TODO: Totem Use and equip every 2 hours 
        # TODO: Familiar
        # TODO: Anti bot alert
        # TODO: CC For better Burning
        # TODO: EB spawn handler