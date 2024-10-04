from pygame.surface import Surface

from Configures import *


class BaseWidget(Surface):
    rect = None

    def __init__(self, surface, size):
        Surface.__init__(self, size, SRCALPHA)
        self.surface = surface

    def draw(self):
        self.surface.blit(self, self.rect)

    def center(self, correct=None, direction=(True, True)):
        width, height = self.surface.get_size()
        if direction[0]:
            self.rect.centerx = (width // 2)
        if direction[1]:
            self.rect.centery = (height // 2)
        if correct is not None:
            self.rect.move_ip(correct)

    def detect_event(self, event):
        if self.rect.collidepoint(event.pos):
            return STATUS_HOVER
