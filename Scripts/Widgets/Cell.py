from pygame import draw

from Configures import *
from Scripts.Widgets.Base import BaseWidget
from Scripts.Widgets.Text import TextWidget


class CellWidget(BaseWidget):
    color, text = None, None

    def __init__(self, surface, text, size, coordinate, color=None):
        BaseWidget.__init__(self, surface, size)
        self.coordinate = coordinate
        self.rect = self.get_rect()
        self.rect.move_ip(coordinate)
        self.text = TextWidget(self, text, 50, color=COLOR_GRAY)
        self.update(color=COLOR_DARK_FLESH if color is None else color)

    def move(self, cell=None, coordinate=None):
        if cell is not None:
            self.rect.topleft = cell.rect.topleft
            return None
        self.rect.topleft = coordinate if coordinate is not None else self.coordinate

    def update(self, text=None, color=None):
        if text is not None:
            self.text.update(text)
            self.text.center()
        if color is not None:
            self.color = color
        self.fill(SRCALPHA)
        draw.rect(self, self.color, ((0, 0), self.rect.size), 0, 5)
        self.text.draw()
