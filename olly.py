import csv

count1 = 0
count2 = 0
a = 0

def esc(code):
    return f'\u001b[{code}m'


def flag_cz():
    for i in range(3):
        print(RED + '  ' * (20) + END)

    for i in range(3):
        print(WHITE + '  ' * (20) + END)

    for i in range(3):
        print(BLUE + '  ' * (20) + END)


def usor():
    print(BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (
        1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + END)
    print(WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (
        1) + BLACK + '  ' * (1) + WHITE + '  ' * (1)
          + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (
              1) + WHITE + '  ' * (1) + END)
    print(WHITE + '  ' * (2) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (
        3) + BLACK + '  ' * (
              1) + WHITE + '  ' * (2) + END)
    print(WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (
        1) + BLACK + '  ' * (1) + WHITE + '  ' * (1)
          + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + BLACK + '  ' * (
              1) + WHITE + '  ' * (1) + END)
    print(BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + BLACK + '  ' * (
        1) + WHITE + '  ' * (3) + BLACK + '  ' * (1) + END)


def func():
    print(END)
    print(18, WHITE + '  ' * (8) + BLACK + '  ' * (1) + END)
    print(17, WHITE + '  ' * (8) + BLACK + '  ' * (1) + END)
    print(16, WHITE + '  ' * (7) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + END)
    print(15, WHITE + '  ' * (7) + BLACK + '  ' * (1) + WHITE + '  ' * (1) + END)
    print(14, WHITE + '  ' * (6) + BLACK + '  ' * (1) + WHITE + '  ' * (2) + END)
    print(13, WHITE + '  ' * (6) + BLACK + '  ' * (1) + WHITE + '  ' * (2) + END)
    print(12, WHITE + '  ' * (5) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + END)
    print(11, WHITE + '  ' * (5) + BLACK + '  ' * (1) + WHITE + '  ' * (3) + END)
    print(10, WHITE + '  ' * (4) + BLACK + '  ' * (1) + WHITE + '  ' * (4) + END)
    print(9, '', WHITE + '  ' * (4) + BLACK + '  ' * (1) + WHITE + '  ' * (4) + END)
    print(8, '', WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (5) + END)
    print(7, '', WHITE + '  ' * (3) + BLACK + '  ' * (1) + WHITE + '  ' * (5) + END)
    print(6, '', WHITE + '  ' * (2) + BLACK + '  ' * (1) + WHITE + '  ' * (6) + END)
    print(5, '', WHITE + '  ' * (2) + BLACK + '  ' * (1) + WHITE + '  ' * (6) + END)
    print(4, '', WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (7) + END)
    print(3, '', WHITE + '  ' * (1) + BLACK + '  ' * (1) + WHITE + '  ' * (7) + END)
    print(2, '', BLACK + '  ' * (1) + WHITE + '  ' * (8) + END)
    print(1, '', BLACK + '  ' * (1) + WHITE + '  ' * (8) + END)


'''def array_init(array_in, st):
    for i in range(10):
        for j in range(10):
            if j == 0:
                array_in[i][j] = round(st * (8 - i) + st, 1)
            if i == 9:
                array_in[i][j] = round(j, 1)
    return array_in


def array_fill(array_fi, res, st):
    for i in range(9):
        for k in range(10):
            if abs(array_fi[i][0] - res[9 - k]) < st:
                for j in range(9):
                    if 8 - j == k:
                        array_fi[i][j + 1] = 1
    return array_fi


def print_plot(plot):
    for i in range(9):
        line = ''
        for j in range(10):
            if j == 0:
                line += WHITE + str(plot[i][j])
            if plot[i][j] == 0:
                line += '  '
            elif plot[i][j] == 1:
                line += RED + '  ' + WHITE
        line += END
        print(line)
    print(WHITE + '0   1 2 3 4 5 6 7 8 9' + END)'''

RED = esc(41)
BLUE = esc(44)
WHITE = esc(40)
END = esc(0)
BLACK = esc(107)

flag_cz()
usor()
print('', 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
func()

with open('books.csv', 'r', encoding='cp1251') as csvfile:
    table = csv.reader(csvfile, delimiter=';')
    for row in table:
        if a != 0:
            if row[6][6:10] <= '2016':
                count1 += 1
            else:
                count2 += 1
        a += 1
print(count1)
print(count2)

per1 = int((count1/(count1+count2))*100)
print(per1)
per2 = 100 - per1
print(per2)
print(f'   До 2016 {BLACK}{"  " * per1}{END}{per1}%')
print(f'После 2016 {WHITE}{"  " * per2}{END}{"  " *(per1-per2)}{per2}%')