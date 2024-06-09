# dirs
# 0 1 2
# 3 X 4
# 5 6 7

class Fig:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.neighbours = [None] * 8

    def __str__(self):
        neighbs = ''
        for f in self.neighbours:
            if not f is None:
                neighbs += f'({f.x}, {f.y}) '
            else:
                neighbs += 'None '
        return f'({self.x}, {self.y}): {neighbs}'

    def __repr__(self):
        return self.__str__()

    def seeing_fig(self, other, si, oi):
        self.neighbours[si] = other
        other.neighbours[oi] = self

    def line_5(self):
        for (i, j) in [(0, 7), (1, 6), (2, 5), (3, 4)]:
            line = self.line_dir(i) + self.line_dir(j) - 1
            if line == 5:
                return True
        return False

    def line_dir(self, dir):
        if (self.neighbours[dir] is None) or (self.y == 0 and dir in [0, 3, 5]) or (self.x == 0 and dir in [0, 1, 2]):
            return 1
        return self.neighbours[dir].line_dir(dir) + 1


def add_neighbours(all_figs, x, ind_y):
    fig = all_figs[x][ind_y]
    y = fig.y
    if ind_y - 1 >= 0 and all_figs[x][ind_y - 1].y == y - 1:
        fig.seeing_fig(all_figs[x][ind_y - 1], 3, 4)
    if ind_y + 1 < len(all_figs[x]) and all_figs[x][ind_y + 1].y == y + 1:
        fig.seeing_fig(all_figs[x][ind_y + 1], 4, 3)

    x_cur = x - 1
    if x_cur in all_figs.keys():
        for i in range(len(all_figs[x_cur])):
            curf = all_figs[x_cur][i]
            if curf.y == y - 1:
                fig.seeing_fig(curf, 0, 7)
            elif curf.y == y:
                fig.seeing_fig(curf, 1, 6)
            elif curf.y == y + 1:
                fig.seeing_fig(curf, 2, 5)

    x_cur = x + 1
    if x_cur in all_figs.keys():
        for i in range(len(all_figs[x_cur])):
            curf = all_figs[x_cur][i]
            if curf.y == y - 1:
                fig.seeing_fig(curf, 5, 2)
            elif curf.y == y:
                fig.seeing_fig(curf, 6, 1)
            elif curf.y == y + 1:
                fig.seeing_fig(curf, 7, 0)


def append_fig_arr(all_figs, fig):
    x, y = fig.x, fig.y
    if x not in all_figs.keys():
        i = 0
        all_figs[x] = [fig]
    else:
        all_figs[x].append(fig)
        i = len(all_figs[x]) - 1
        while i - 1 >= 0 and all_figs[x][i - 1].y > all_figs[x][i].y:
            all_figs[x][i - 1], all_figs[x][i] = all_figs[x][i], all_figs[x][i - 1]
            i -= 1

    add_neighbours(all_figs, x, i)


def print_all_figs(figs):
    for k in figs.keys():
        print(f'{k}: ')
        for i in range(len(figs[k])):
            print(f'\t{figs[k][i]}')


def main():
    # {x1: (y1, y2, ...), x2: (y1, y2)}
    all_figs_x = dict()
    all_figs_y = dict()

    n = int(input())
    for k in range(n):
        x, y = map(int, input().split())
        fig = Fig(x, y)

        if k % 2 == 0:
            append_fig_arr(all_figs_x, fig)
            if fig.line_5():
                if k == n - 1:
                    print('First')
                else:
                    print('Inattention')
                return
        else:
            append_fig_arr(all_figs_y, fig)
            if fig.line_5():
                if k == n - 1:
                    print('Second')
                else:
                    print('Inattention')
                return

    # print_all_figs(all_figs_x)
    # print(find_5(all_figs_x, True))

    print('Draw')
    return

main()
