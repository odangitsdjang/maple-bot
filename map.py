import time
import random
from rune_solver import find_arrow_directions

class Map:
    def __init__(self, player, game):
        self.g = game
        self.p = player
    def solve_rune(self, target):
        """
        Given the (x, y) location of a rune, the bot will attempt to move the player to the rune and solve it.
        """
        while True:
            p = self.p
            g = self.g
            print("Pathing towards rune...")
            p.go_to(target)
            # Activate the rune.
            time.sleep(1)
            p.press("SPACE")
            # Take a picture of the rune.
            time.sleep(1)
            img = g.get_rune_image()
            print("Attempting to solve rune...")
            directions = find_arrow_directions(img)

            if len(directions) == 4:
                print(f"Directions: {directions}.")
                for d, _ in directions:
                    p.press(d)

                # The player dot will be blocking the rune dot, attempt to move left/right to unblock it.
                p.hold("LEFT")
                time.sleep(random.uniform(0.5, 1.25))
                p.release("LEFT")

                p.hold("RIGHT")
                time.sleep(random.uniform(0.5, 1.25))
                p.release("RIGHT")

                rune_location = g.get_rune_location()
                if rune_location is None:
                    print("Rune has been solved.")
                    break
                else:
                    print("Trying again...")

    # TODO: refactor even more s.t. the logic is in player - so different players can run the map differently
    def run_sss1(self):
        target = (97.5, 48.5)
        time_90 = time.time()
        time_120 = time_90
        
        p = self.p
        g = self.g
        # cast 120sec buffs
        # TODO: move 90/120 buff keys to tuple
        # TODO: add functionality to start the bot with no rune for first 15 mins 
        p.cast_buffs(("2", "3", "6"))

        while True:
            # TODO: refactor g.check_other_player, g.check_rune
            other_location = g.get_other_location()
            if other_location > 0:
                print("A player has entered your map.")

            rune_location = g.get_rune_location()
            # TODO: improve rune accuracy - works on 1024x768 resolution 
            if rune_location is not None:
                print("A rune has appeared.")
                solve_rune(rune_location)

            print("Running...")
            current = time.time()
            elapsed_90  = current - time_90
            elapsed_120 = current - time_120
            print(f"elapsed_90: {elapsed_90}, elapsed_120: {elapsed_120}, time_90: {time_90}, time_120: {time_120}")
            if current - time_90 > 90:
                p.cast_buffs(("Q", "W", "1"))
                time_90 = current
            if current - time_120 > 120: 
                p.cast_buffs(("2", "3", "6"))
                time_120 = current

            p.go_to(target)
            time.sleep(0.5)
        
            for interval in range(3):
                p.press("ALT")
                time.sleep(0.1)
                p.press("SHIFT")
                time.sleep(0.3)
                if interval % 2 == 0:
                    p.press("RIGHT")
                else:
                    p.press("LEFT")
        
            time.sleep(1)
      
            p.press("UP")
            time.sleep(0.5)
            for _ in range(3):
                p.press("RIGHT")
                p.press("SHIFT")
                time.sleep(0.5)
        
            # move back to go through portal to initial position
            p.press("LEFT")
            time.sleep(1)
            p.press("UP")
            time.sleep(2)

    def run_es(self):
        # initial bottom left
        target = (7.5, 31.5)
        time_90 = time.time()
        time_120 = time_90
        p = self.p
        g = self.g
        # cast 120sec buffs
        # TODO: move 90/120 buff keys to tuple
        # TODO: add functionality to start the bot with no rune for first 15 mins 
        p.cast_buffs(("2", "3", "6"))

        while True:
            # TODO: refactor g.check_other_player, g.check_rune
            other_location = g.get_other_location()
            if other_location > 0:
                print("A player has entered your map.")

            # TODO: improve rune accuracy - works on 1024x768 resolution 
            rune_location = g.get_rune_location()
            if rune_location is not None:
                print("A rune has appeared.")
                self.solve_rune(rune_location)

            print("Running...")

            current = time.time()
            elapsed_90  = current - time_90
            elapsed_120 = current - time_120
            print(f"elapsed_90: {elapsed_90}, elapsed_120: {elapsed_120}, time_90: {time_90}, time_120: {time_120}")
            if current - time_90 > 90:
                p.cast_buffs(("Q", "W", "1"))
                time_90 = current
            if current - time_120 > 120: 
                p.cast_buffs(("2", "3", "6"))
                time_120 = current

            p.go_to(target)
            time.sleep(0.5)
        
            for interval in range(3):
                p.press("RIGHT")
                time.sleep(1)
                # TODO: BM double jump attack 
                for _ in range(6):
                    p.press("ALT")
                    time.sleep(0.1)
                    p.press("ALT")
                    time.sleep(0.1)
                    p.press("SHIFT")
                    time.sleep(0.6)
                p.press("LEFT")
                time.sleep(0.5)

                for _ in range(6):
                    p.press("ALT")
                    time.sleep(0.1)
                    p.press("ALT")
                    time.sleep(0.1)
                    p.press("SHIFT")
                    time.sleep(0.6) #0.6 - 0.7
        
            time.sleep(0.5) # 0.5-1
      