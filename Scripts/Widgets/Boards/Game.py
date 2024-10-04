from pygame import draw

from Configures import *
from Scripts.Widgets.Base import BaseWidget
from Scripts.Widgets.Cell import CellWidget


class GameBoard(BaseWidget):
    cells = []
    empty_cell = None

    def __init__(self, surface, coordinate, size, cell_size):
        BaseWidget.__init__(self, surface, WINDOW_SIZE)
        self.rect = self.get_rect()
        copy_coordinate = list(coordinate)
        spacing = ((340 - (cell_size * size)) / (size + 1))
        for _ in range(size):
            row_cells = []
            for __ in range(size):
                row_cells.append(CellWidget(self, '', (cell_size, cell_size), copy_coordinate))
                copy_coordinate[0] += (spacing + cell_size)
            copy_coordinate[0] = coordinate[0]
            copy_coordinate[1] += (spacing + cell_size)
            self.cells.append(row_cells)

    def stroke_cell(self):
        self.update()
        draw.rect(self, COLOR_GRAY, self.empty_cell.rect, 2, 5)

    def detect_overlap(self, rect):
        return self.empty_cell.rect.colliderect(rect)

    def update(self, question=None):
        if question is not None:
            for row, cells in enumerate(self.cells):
                for column, cell in enumerate(cells):
                    text = question['title'][row][column]
                    cell.update(text, COLOR_DARK_FLESH if text else COLOR_LIGHT_FLESH)
            row, column = question['answer'][0]
            self.empty_cell = self.cells[row][column]
            self.empty_cell.update(color=COLOR_WHITE)
        self.fill(SRCALPHA)
        for row_cells in self.cells:
            for cell in row_cells:
                cell.draw()

