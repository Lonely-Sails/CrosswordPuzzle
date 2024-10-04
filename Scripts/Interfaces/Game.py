from pygame import Surface, mouse, draw

from Configures import *
from Scripts.Uitls import number_chinese
from Scripts.Interfaces.Masks import ResultMask
from Scripts.Widgets import TextWidget
from Scripts.Widgets.Boards import ChoicesBoard, GameBoard


class GameInterface(Surface):
    flag = False
    offest, cell, answer = None, None, None

    def __init__(self):
        Surface.__init__(self, WINDOW_SIZE, SRCALPHA)
        self.wining_mask = ResultMask(self, RESOURCES_IMAGE_WINING)
        self.failure_mask = ResultMask(self, RESOURCES_IMAGE_FAILURE)
        self.level_text = TextWidget(self, '', 23, (0, 7))
        self.game_board = GameBoard(self, (34, 79), 4, 80)
        self.choices_board = ChoicesBoard(self, (34, 470), (2, 4), 80)
        self.update()

    def event(self, event):
        if event.type == MOUSEBUTTONDOWN:
            cell = self.choices_board.detect_event(event)
            if cell is not None:
                self.cell, self.flag = cell, True
                self.offest = (event.pos[0] - cell.rect.left, event.pos[1] - cell.rect.top)
                self.choices_board.cells.remove(cell)
                self.choices_board.cells.append(cell)
                mouse.set_cursor(SYSTEM_CURSOR_HAND)
        elif self.flag:
            if event.type == MOUSEMOTION:
                if self.game_board.detect_overlap(self.cell):
                    self.game_board.stroke_cell()
                else:
                    self.game_board.update()
                self.cell.move(coordinate=(event.pos[0] - self.offest[0], event.pos[1] - self.offest[1]))
                self.update()
            elif event.type == MOUSEBUTTONUP:
                self.flag = False
                mouse.set_cursor(SYSTEM_CURSOR_ARROW)
                if self.game_board.detect_overlap(self.cell):
                    self.cell.move(self.game_board.empty_cell)
                    self.update()
                    if self.cell.text.text == self.answer:
                        return STATUS_SECONDARY_WINING
                    return STATUS_SECONDARY_FAILURE
                self.cell.move()
            self.choices_board.update()
            self.update()

    def update(self):
        self.fill(SRCALPHA)
        draw.rect(self, COLOR_CYAN, ((0, 0), (400, 45)), 0, border_bottom_right_radius=10, border_bottom_left_radius=10)
        draw.rect(self, COLOR_FLESH, ((20, 65), (360, 360)), 0, 10)
        draw.rect(self, COLOR_FLESH, ((0, 450), (400, 200)), 0, border_top_right_radius=10, border_top_left_radius=10)
        self.game_board.draw()
        self.choices_board.draw()
        self.level_text.draw()

    def update_game(self, question, level):
        self.answer = question['answer'][1]
        self.game_board.update(question)
        self.choices_board.update(question)
        self.level_text.update(F'第 {number_chinese(str(level))} 关')
        self.level_text.center(direction=(True, False))
