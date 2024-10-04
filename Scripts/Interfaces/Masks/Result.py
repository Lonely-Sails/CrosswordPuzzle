from webbrowser import open as open_page
from pygame import Surface, mouse

from Configures import *
from Scripts.Uitls import number_chinese, load_image
from Scripts.Widgets import ButtonWidget, TextWidget


class ResultMask(Surface):
    def __init__(self, surface, path):
        Surface.__init__(self, WINDOW_SIZE, SRCALPHA)
        self.surface = surface
        self.image = load_image(path, 0.55)
        self.rect = self.image.get_rect()
        self.rect.centerx = (WINDOW_WIDTH / 2)
        self.rect.centery = (WINDOW_HEIGHT / 2)
        self.back_button = ButtonWidget(self, '返回', COLOR_ORANGE, (45, 470), (140, 40))
        self.continue_button = ButtonWidget(self, '继续', COLOR_CYAN, (215, 470), (140, 40))
        coordinate = 240
        self.tip_texts = []
        for _ in range(2):
            coordinate += 27
            self.tip_texts.append(TextWidget(self, '', 25, (0, coordinate), COLOR_BLACK))
        self.update()

    def update(self, question=None, level=None):
        if question is not None:
            if level is not None:
                question['tip'] = ('可喜可贺！', F'你进入到了第 {number_chinese(str(level))} 关')
            for index, tip in enumerate(question['tip']):
                self.tip_texts[index].update(tip)
                self.tip_texts[index].center(direction=(True, False))
        self.fill(COLOR_MASK)
        self.blit(self.image, self.rect)
        self.back_button.draw()
        self.continue_button.draw()
        for text in self.tip_texts:
            text.draw()

    def event(self, event):
        if event.type == MOUSEMOTION:
            if len(self.tip_texts[0].text) == 4:
                for text in self.tip_texts:
                    status = text.detect_event(event)
                    if status is not None:
                        mouse.set_cursor(SYSTEM_CURSOR_HAND)
                        return None
                    mouse.set_cursor(SYSTEM_CURSOR_ARROW)
            status = self.back_button.detect_event(event)
            self.back_button.update(status)
            if status is not None:
                mouse.set_cursor(SYSTEM_CURSOR_HAND)
                return None
            mouse.set_cursor(SYSTEM_CURSOR_ARROW)
            status = self.continue_button.detect_event(event)
            self.continue_button.update(status)
            if status is not None:
                mouse.set_cursor(SYSTEM_CURSOR_HAND)
                return None
            mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        elif event.type == MOUSEBUTTONDOWN:
            mouse.set_cursor(SYSTEM_CURSOR_ARROW)
            if len(self.tip_texts[0].text) == 4:
                for text in self.tip_texts:
                    status = text.detect_event(event)
                    if status is not None:
                        open_page(F'https://hanyu.baidu.com/zici/s?wd={text.text}')
                        return None
            if self.back_button.detect_event(event):
                return STATUS_HOME
            if self.continue_button.detect_event(event):
                return STATUS_GAME
