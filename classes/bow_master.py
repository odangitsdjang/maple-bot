from player import Player
import time
import random

class BowMaster(Player):
    def __init__(self, context, device, game, buff_90, buff_120):
        self.buff_90 = buff_90;
        self.buff_120 = buff_120;

        Player.__init__(self, context, device, game)

    # override
    def jump_up(self):
        self.jump()
        self.press("UP")
        self.press("UP")

    def run_es(self):
        # initial bottom left
        target = (18, 31.5)
        time_90 = time.time()
        time_120 = time_90
        p = self.p
        g = self.g

        # TODO: add functionality to start the bot with no rune for first 15 mins
        p.cast_buffs(self.buff_120)

        while True:
            # TODO: refactor g.check_other_player, g.check_rune
            other_location = g.get_other_location()
            if other_location > 0:
                print("A player has entered your map.")

            # TODO: improve rune accuracy - Coded for 800x600, but also works on 1024x768 resolution
            # TODO: Rune 15 min timer to skip this logic for improved performance - currently testing performance
            # TODO: if rune on cd, continue
            current = time.time()
            rune_location = g.get_rune_location()
            if rune_location is not None:
                print("A rune has appeared.")
                self.solve_rune(rune_location)
            current2 = time.time()
            print(f"Rune check took {current2-current} seconds")
            print("Running...")

            current = time.time()
            elapsed_90 = current - time_90
            elapsed_120 = current - time_120
            print(f"elapsed_90: {elapsed_90}, elapsed_120: {elapsed_120}")
            if elapsed_90 > 90:
                p.cast_buffs(self.buff_90)
                time_90 = current
            if elapsed_120 > 120:
                p.cast_buffs(self.buff_120)
                time_120 = current

            p.go_to(target)
            time.sleep(random.uniform(0.4, 0.6))

            # each loop takes ~14s
            for interval in range(2):
                p.hold("RIGHT")
                for _ in range(5):
                    p.double_jump_att()
                p.release("RIGHT")
                time.sleep(random.uniform(0.4, 0.6))
                p.hold("LEFT")
                for _ in range(5):
                    p.double_jump_att()
                p.release("LEFT")
                time.sleep(random.uniform(0.4, 0.6))
            time.sleep(random.uniform(0.4, 0.6))
