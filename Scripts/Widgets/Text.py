from pygame import Surface
from pygame.font import Font

from Configures import *
from Scripts.Widgets.Base import BaseWidget


class TextWidget(BaseWidget):
    text = None

    def __init__(self, surface, text, size, coordinate=None, color=None, path=None):
        BaseWidget.__init__(self, surface, WINDOW_SIZE)
        self.color = COLOR_WHITE if color is None else color
        self.coordinate = (0, 0) if coordinate is None else coordinate
        self.font = Font(RESOURCES_FONT_MAIN if path is None else path, size)
        self.update(text)

    def update(self, text, underline=False):
        self.text = text
        render = self.font.render(text, True, self.color)
        self.rect = render.get_rect()
        self.rect.move_ip(self.coordinate)
        self.fill(SRCALPHA)
        self.blit(render, (0, 0))

    def stroke_text(self, color, width=3):
        stroke = self.font.render(self.text, True, color)
        self.rect.width = ((width * 2) + self.rect.width)
        self.rect.height = ((width * 2) + self.rect.height)
        temp_render = Surface(self.rect.size, SRCALPHA)
        for row in (-1, 0, 1):
            for column in (-1, 0, 1):
                if column and row:
                    for number in range(width):
                        temp_render.blit(stroke, ((number * row) +
                                    width, (number * column) + width))
        temp_render.blit(self, (width, width))
        self.fill(SRCALPHA)
        self.blit(temp_render, (0, 0))
