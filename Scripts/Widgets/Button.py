from pygame import draw
from pygame.surface import Surface

from Configures import *
from Scripts.Widgets.Text import TextWidget
from Scripts.Widgets.Base import BaseWidget


class ButtonWidget(BaseWidget):
    color, size = None, None

    def __init__(self, surface, text, color, coordinate=None, size=(160, 45)):
        BaseWidget.__init__(self, surface,  (size[0] + 3, size[1] + 3))
        self.color, self.size = color, size
        self.rect = self.get_rect()
        self.rect.move_ip(coordinate if coordinate else (0, 0))
        self.text = TextWidget(self, text, 25)
        self.text.center((-2, -3))
        self.update(STATUS_INITIALIZTION)

    def update(self, status=None):
        self.fill(SRCALPHA)
        if status == STATUS_HOVER:
            draw.rect(self, COLOR_SHADOW, ((3, 3), self.size), 0, 15)
        draw.rect(self, self.color, ((0, 0), self.size), 0, 15)
        draw.rect(self, COLOR_WHITE, ((0, 0), self.size), 3, 15)
        draw.rect(self, COLOR_GRAY, ((0, 0), self.size), 1, 15)
        self.text.draw()
        if status != STATUS_INITIALIZTION:
            self.surface.update()
