from random import randint, choice

from Configures import *
from Scripts.Interfaces.Background.Word import BackgroundWord


class Background:
    words = []
    word_strings = None

    def __init__(self, screen, word_strings):
        self.screen = screen
        self.word_strings = word_strings
        for _ in range(4):
            self.words.append(self.create_word())

    def update(self):
        self.screen.fill(COLOR_BACKGROUND)
        for word in self.words:
            word.draw()
            if word.update_word():
                self.words.remove(word)
                new_word = self.create_word()
                self.words.append(new_word)

    def create_word(self):
        word = choice(self.word_strings)
        coordinate = ((randint(-10, (WINDOW_WIDTH - 10))), (randint(-10, (WINDOW_HEIGHT - 10))))
        new_word = BackgroundWord(self.screen, coordinate, word)
        return new_word
