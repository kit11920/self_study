
class BlockWordEmbedded:
    def __init__(self, w, h):
        self.width = w
        self.height = h

        self.x = self.y = 0
        self.xe = self.ye = 0

    def __str__(self):
        return f'Embedded(w={self.width} h={self.height})'

    def __repr__(self):
        return self.__str__()


class Word(BlockWordEmbedded):
    def __init__(self, text, h, c):
        super().__init__(len(text) * c, h)
        self.text = text
        self.x = self.y = 0
        self.xe = self.ye = 0

    def __str__(self):
        return f'Word(text="{self.text}" w={self.width} h={self.height})'

    def __repr__(self):
        return self.__str__()


class Surrounded:
    def __init__(self, w, h):
        self.width = w
        self.height = h
        self.x = self.y = 0
        self.xe = self.ye = 0

    def __str__(self):
        return f'Surrounded(w={self.width} h={self.height})'

    def __repr__(self):
        return self.__str__()


class Floating:
    def __init__(self, w, h, dx, dy):
        self.width = w
        self.height = h
        self.dx = dx
        self.dy = dy
        self.x = self.y = 0
        self.xe = self.ye = 0

    def __str__(self):
        return f'Floating(w={self.width} h={self.height} dx={self.dx} dy={self.dy})'

    def __repr__(self):
        return self.__str__()


class EmptyLine:
    def __str__(self):
        return 'EmptyLine()'

    def __repr__(self):
        return self.__str__()


class Dword:
    def __init__(self, w, h, c):
        self.page_width = w
        self.line_height = h
        self.char_width = c

        self.last_sur = False
        self.x = 0
        self.y_line = 0
        self.y_next_line = self.line_height
        self.surrounds = list()
        self.floating_x = self.floating_y = 0

        self.images_coord = list()

    def del_surrounds_higher(self):
        # удаляем surrounds которые выше
        i = 0
        while i < len(self.surrounds):
            if self.surrounds[i].ye <= self.y_line:
                del self.surrounds[i]
            else:
                i += 1

    def if_last_surround(self):
        for i in range(len(self.surrounds)):
            if self.x == self.surrounds[i].xe:
                return True
        return False

    def good_interval(self, end, width, need_space=False):
        if need_space and self.x != 0 and not self.if_last_surround():
            return end - self.x >= width + self.char_width
        else:
            return end - self.x >= width

    # возвращает надо ли слову ставить пробел перед
    def find_fragment(self, width, need_space):
        i = 0
        while i < len(self.surrounds) and \
                not self.good_interval(self.surrounds[i].x, width, need_space):
            self.x = max(self.surrounds[i].xe, self.x)
            i += 1

        if i == len(self.surrounds) and \
                not self.good_interval(self.page_width, width, need_space):
            # переход на новую строку
            self.y_line = self.y_next_line
            self.floating_y = self.y_line
            self.y_next_line = self.y_line + self.line_height
            self.x = 0
            self.del_surrounds_higher()
            self.find_fragment(width, need_space)

    def add_block_word_embedded(self, block):
        self.find_fragment(block.width, True)

        if self.x != 0 and not self.if_last_surround():
            self.x += self.char_width # пробел перед словом
        block.x, block.y = self.x, self.y_line
        block.xe, block.ye = self.x + block.width, self.y_line + block.height
        if block.__class__ != Word:
            self.images_coord.append((self.x, self.y_line))

        if self.y_next_line - self.y_line < block.height:
            self.y_next_line = self.y_line + block.height

        self.x += block.width
        self.floating_x = self.x

    def add_surrounded(self, img):
        self.find_fragment(img.width, False)

        img.x, img.y = self.x, self.y_line
        img.xe, img.ye = self.x + img.width, self.y_line + img.height
        self.images_coord.append((img.x, img.y))

        # вставляет по возрастанию x
        self.surrounds.append(img)
        i = len(self.surrounds) - 1
        while i - 1 > 0 and self.surrounds[i].x > self.surrounds[i - 1].x:
            self.surrounds[i], self.surrounds[i - 1] = self.surrounds[i - 1], self.surrounds[i]
            i -= 1

        self.x += img.width
        self.floating_x = self.x

    def add_floating(self, img):
        # print(self.x, self.y_line, self.floating_x, self.floating_y)
        ximg, yimg = self.floating_x + img.dx, self.floating_y + img.dy
        if ximg < 0: ximg = 0
        if ximg + img.width > self.page_width: ximg = self.page_width - img.width

        img.x, img.y = ximg, yimg
        img.xe, img.ye = ximg + img.width, yimg + img.height
        self.images_coord.append((img.x, img.y))

        self.floating_x = max(self.floating_x, img.xe)
        self.floating_y = yimg

    def add_empty_line(self):
        next_y = max([self.y_next_line] + [sur.xe for sur in self.surrounds])
        self.y_line = next_y
        self.floating_y = self.y_line
        self.x = 0

    def print_images_coord(self):
        for i in range(len(self.images_coord)):
            print(*self.images_coord[i])
        print()


def image_input(text):
    layout = ''
    w = h = dx = dy = 0
    text = text.split()
    for param in text:
        name, data = param.split('=')
        if name == 'layout': layout = data
        elif name == 'width': w = int(data)
        elif name == 'height': h = int(data)
        elif name == 'dx': dx = int(data)
        elif name == 'dy': dy = int(data)
        else: pass
    if layout == 'embedded': return BlockWordEmbedded(w, h)
    elif layout == 'surrounded': return Surrounded(w, h)
    elif layout == 'floating': return Floating(w, h, dx, dy)
    else: raise Exception('MY Error image input')


def words_input(text, line_height, char_width):
    data = list()
    text = text.split()
    for word in text:
        data.append(Word(word, line_height, char_width))
    return data


def inputter(f, line_height, char_width):
    data = list()
    str = f.readline()
    while str != '':
        # print(f'"{str}"')
        if str == '\n':
            data.append(EmptyLine())
        else:
            str = str.split('(image ')
            if str[0] != '':
                data.extend(words_input(str[0], line_height, char_width))
            del str[0]

            for i in range(len(str)):
                str[i] = str[i].split(')')
                image, text = str[i][0], ')'.join(str[i][1:])
                data.append(image_input(image))
                data.extend(words_input(text, line_height, char_width))

        str = f.readline()
    # for i in range(len(data)):
    #     print(data[i])
    return data


def print_data(data):
    for elem in data:
        if elem.__class__ != EmptyLine:
            print(f'({elem.x}, {elem.y}) - ({elem.xe}, {elem.ye}) - {elem}')
        else:
            print(elem)


def write_text_data(dword, data):
    for elem in data:
        if elem.__class__ == Word or elem.__class__ == BlockWordEmbedded:
            dword.add_block_word_embedded(elem)
        elif elem.__class__ == Surrounded:
            dword.add_surrounded(elem)
        elif elem.__class__ == Floating:
            dword.add_floating(elem)
        else:
            dword.add_empty_line()

    print_data(data)

def main():
    f = open('input.txt', 'r')
    page_width, line_height, char_width = map(int, f.readline().split())
    dword = Dword(page_width, line_height, char_width)

    data = inputter(f, line_height, char_width)
    f.close()

    write_text_data(dword, data)
    dword.print_images_coord()










main()
