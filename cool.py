from math import floor, sin, cos
from time import sleep

screen_width, screen_height = 96, 48

screen_buffer = [ [ '.' for j in range(screen_width)] for i in range(screen_height) ]

def draw_line(x1, y1, x2, y2, char):
    y = y2 - y1
    x = x2 - x1

    ax = abs(x)
    ay = abs(y)

    if ax > ay:
        scalar = y / x
        direction = x // ax

        for i in range(x1, x2 + direction, direction):
            screen_buffer[y1 + floor((i - x1) * scalar)][i] = char

    else:
        scalar = x / y
        direction = y // ay

        for i in range(y1, y2 + direction, direction):
            screen_buffer[i][x1 + floor((i - y1) * scalar)] = char


def show():
    print('+', '-' * screen_width, '+', sep = '')
    for i in range(screen_height):
        print('|', *screen_buffer[i], '|', sep = '')
    print('+', '-' * screen_width, '+', sep = '')

def clear():
    for i in screen_buffer:
        for j in range(screen_width):
            i[j] = '.'

def main():

    cube_vertices = [
         1.0, 1.0, 1.0,
        -1.0, 1.0, 1.0,
        -1.0,-1.0, 1.0,
         1.0,-1.0, 1.0,

         1.0, 1.0,-1.0,
        -1.0, 1.0,-1.0,
        -1.0,-1.0,-1.0,
         1.0,-1.0,-1.0
    ]

    cube_indices = [
        0, 1,
        1, 2,
        2, 3,
        3, 0,

        4, 5,
        5, 6,
        6, 7,
        7, 4,

        0, 4,
        1, 5,
        2, 6,
        3, 7
    ]

    cube_position = (0.0, 0.0,-10.0)

    angle = 0
    cx, cy = screen_width // 2, screen_height // 2

    for i in range(200):
        # clear()
        draw_line(cx + floor(cos(angle) * 20), cy + floor(sin(angle) * 10), cx, cy, '#')
        show()
        angle += 3.14 / 100
        sleep(0.1)

    draw_line(20, 20, 4, 4, '\\')
    show()

main()

