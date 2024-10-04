from pygame import Surface, mouse

from Configures import *
from Scripts.Widgets import ButtonWidget, TextWidget


class HomeInterface(Surface):
    buttons = []
    buttons_status = []

    def __init__(self):
        Surface.__init__(self, WINDOW_SIZE, SRCALPHA)
        self.title = TextWidget(self, '填 字', 100, (60, 40), path=RESOURCES_FONT_OTHER)
        self.small_title = TextWidget(self, '游 戏', 50, (210, 170), path=RESOURCES_FONT_OTHER)
        self.title.stroke_text(COLOR_GRAY)
        self.small_title.stroke_text(COLOR_GRAY)
        buttons_text = ('开始游戏', '游戏选项', '退出游戏')
        for index, text in enumerate(buttons_text):
            button = ButtonWidget(self, text, COLOR_ORANGE if index == 2 else COLOR_CYAN)
            button.center((0, (index * 60) + 370), (True, False))
            self.buttons.append(button)
            self.buttons_status.append(None)
        self.update()

    def update(self):
        self.fill(SRCALPHA)
        self.title.draw()
        self.small_title.draw()
        for button in self.buttons:
            button.draw()

    def event(self, event):
        if event.type == MOUSEMOTION:
            for index in range(len(self.buttons)):
                status = self.buttons[index].detect_event(event)
                if status != self.buttons_status[index]:
                    self.buttons[index].update(status)
                    self.buttons_status[index] = status
                    if status is not None:
                        mouse.set_cursor(SYSTEM_CURSOR_HAND)
                        return None
                    mouse.set_cursor(SYSTEM_CURSOR_ARROW)
        elif event.type == MOUSEBUTTONDOWN:
            if STATUS_HOVER in self.buttons_status:
                mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                index = self.buttons_status.index(STATUS_HOVER)
                return (STATUS_GAME, None, STATUS_QUIT)[index]
