from pygame import time
from random import randint

from Configures import *
from Scripts.Widgets import TextWidget


class BackgroundWord(TextWidget):
    flag = True
    transparency, timer = 0, 0

    def __init__(self, surface, coordinate, word):
        TextWidget.__init__(self, surface, word, randint(60, 100), coordinate, COLOR_WHITE, RESOURCES_FONT_OTHER)
        self.timer = time.get_ticks()
        self.show_time = time.get_ticks()
        self.stay_time = randint(10000, 30000)
        self.set_alpha(self.transparency)

    def update_word(self):
        now_time = time.get_ticks()
        if (now_time - self.timer) >= 10:
            self.set_alpha(self.transparency)
            if self.flag and self.transparency < 10:
                self.transparency += 1
                return None
            if (now_time - self.show_time) >= self.stay_time:
                self.flag = False
                self.transparency -= 1
                if self.transparency <= 0:
                    return True
        self.timer = now_time
