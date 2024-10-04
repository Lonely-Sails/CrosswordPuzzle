from json import load
from random import sample, choice

# from Configures import *


class Generate:
    words = None
    word_strings = None
    mapping = dict()

    def __init__(self):
        # with open(CONFIGURE_WORD_PATH, encoding='Utf-8', mode='r') as file:
        with open('./Words.json', encoding='Utf-8', mode='r') as file:
            self.words = load(file)

    def mapping_word(self):
        temp_mapping = {}
        for index in range(len(self.words)):
            for word in self.words[index]:
                if temp_mapping.get(word) and (index not in temp_mapping[word]):
                    temp_mapping[word].append(index)
                    continue
                temp_mapping[word] = [index]
        for key, value in temp_mapping.items():
            if len(value) >= 2:
                self.mapping[key] = value
        self.word_strings = list(self.mapping.keys())

    def generate_question(self):
        choices = sample(self.word_strings, 8)
        question = [([''] * 4) for _ in range(4)]
        word = choice(choices)
        word_one, word_two = (self.words[index] for index in sample(self.mapping[word], 2))
        column, row = word_one.index(word), word_two.index(word)
        question[row] = list(word_one)
        for index in range(4):
            question[index][column] = word_two[index]
        question[row][column] = ''
        return {'choices': choices, 'title': question, 'answer': ((row, column), word), 'tip': (word_one, word_two)}


if __name__ == '__main__':
    Generate = Generate()
    Generate.mapping_word()
    print(Generate.generate_question())