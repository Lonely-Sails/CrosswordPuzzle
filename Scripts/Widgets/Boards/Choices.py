from Configures import *
from Scripts.Widgets.Base import BaseWidget
from Scripts.Widgets.Cell import CellWidget


class ChoicesBoard(BaseWidget):
    cells = []

    def __init__(self, surface, coordinate, size, cell_size):
        BaseWidget.__init__(self, surface, WINDOW_SIZE)
        self.rect = self.get_rect()
        row, column = size
        copy_coordinate = list(coordinate)
        spacing = ((340 - (cell_size * column)) / (column + 1))
        for _ in range(row):
            for __ in range(column):
                cell = CellWidget(self, '', (cell_size, cell_size), tuple(copy_coordinate))
                self.cells.append(cell)
                copy_coordinate[0] += (spacing + cell_size)
            copy_coordinate[0] = coordinate[0]
            copy_coordinate[1] += (spacing + cell_size)

    def back_cells(self):
        for cell in self.cells:
            cell.move()

    def update(self, question=None):
        if question is not None:
            for index, text in enumerate(question['choices']):
                self.cells[index].update(text)
        self.fill(SRCALPHA)
        for cell in self.cells:
            cell.draw()
        self.surface.update()

    def detect_event(self, event):
        for cell in self.cells:
            if cell.detect_event(event):
                return cell
