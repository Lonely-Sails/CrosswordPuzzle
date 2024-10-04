from pygame.image import load
from pygame.transform import smoothscale


number_unit = '十百千万'
number_mapping = '零一二三四五六七八九'

def load_image(path, rate):
    image = load(path)
    image = image.convert_alpha()
    width, height = image.get_size()
    return smoothscale(image, ((width * rate), (height * rate)))

def number_chinese(number):
    result = str()
    length = len(number)
    for index in range(length):
        if number[index - 1] != '0' or number[index] != '0':
            if (length != 2 or index != 0) or number[index] != '1':
                result += number_mapping[int(number[index])]
        if number[index] != '0' and index < (length - 1):
            result += number_unit[length - index - 2]
    if number[-1] == '0':
        result = result[:-1]
    return result


if __name__ == '__main__':
    print(number_chinese(input()))
