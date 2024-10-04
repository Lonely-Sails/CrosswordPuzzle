import pygame
from sys import exit
from os import environ

from Configures import *
from Scripts.File import Config
from Scripts.Generate import Generate
from Scripts.Interfaces import HomeInterface, GameInterface
from Scripts.Interfaces.Background import Background


class CrosswordPuzzle:
    status = STATUS_HOME
    secondary_status = None

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('填字游戏')
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(WINDOW_SIZE)
        self.config = Config()
        self.generate = Generate()
        self.generate.mapping_word()
        self.home_interface = HomeInterface()
        self.game_interface = GameInterface()
        self.background = Background(self.screen, self.generate.word_strings)
        self.reset_game()

    def reset_game(self):
        question = self.generate.generate_question()
        self.game_interface.choices_board.back_cells()
        self.game_interface.failure_mask.update(question)
        self.game_interface.wining_mask.update(question, self.config.level + 1)
        self.game_interface.update_game(question, self.config.level)
        self.game_interface.update()

    def main_loop(self):
        while True:
            self.update()
            self.clock.tick(60)
            pygame.display.flip()
            if self.status == STATUS_QUIT:
                self.config.save()
                pygame.quit()
                exit()
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.config.save()
                    pygame.quit()
                    exit()
                self.manage_event(event)

    def update(self):
        self.background.update()
        if self.status == STATUS_HOME:
            self.screen.blit(self.home_interface, (0, 0))
        elif self.status == STATUS_GAME:
            self.screen.blit(self.game_interface, (0, 0))
            if self.secondary_status == STATUS_SECONDARY_WINING:
                self.screen.blit(self.game_interface.wining_mask, (0, 0))
            elif self.secondary_status == STATUS_SECONDARY_FAILURE:
                self.screen.blit(self.game_interface.failure_mask, (0, 0))
    
    def manage_event(self, event):
        if self.status == STATUS_HOME:
            event = self.home_interface.event(event)
            if event is not None:
                self.status = event
        elif self.status == STATUS_GAME:
            if self.secondary_status == STATUS_SECONDARY_WINING:
                event = self.game_interface.wining_mask.event(event)
                if event is not None:
                    self.status = event
                    self.secondary_status = None
                    self.config.level += 1
                    self.reset_game()
                return None
            elif self.secondary_status == STATUS_SECONDARY_FAILURE:
                event = self.game_interface.failure_mask.event(event)
                if event is not None:
                    self.status = event
                    self.secondary_status = None
                    self.reset_game()
                return None
            event = self.game_interface.event(event)
            if event is not None:
                if event >= 10:
                    self.status = event
                    return None
                self.secondary_status = event


if __name__ == '__main__':
    environ['SDL_VIDEO_CENTERED'] = '1'
    CrosswordPuzzle().main_loop()
