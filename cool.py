from math import floor, sin, cos, tan, pi
from time import sleep
import os
from os import system

def todo():
    print('todo')

screen_width, screen_height = 96, 48
fov = pi / 2

CLEAR_COMMAND = 'clear' if os.name == 'posix' else 'clr'

screen_buffer = [ [ ' ' for j in range(screen_width)] for i in range(screen_height) ]


def draw_line(x1, y1, x2, y2, char):
    y = y2 - y1
    x = x2 - x1

    ax = abs(x)
    ay = abs(y)

    if ax > ay:
        scalar = y / x
        direction = x // ax

        for i in range(x1, x2 + direction, direction):
            screen_buffer[y1 + int(round((i - x1) * scalar))][i] = char

    else:
        scalar = x / y
        direction = y // ay

        for i in range(y1, y2 + direction, direction):
            screen_buffer[i][x1 + int(round((i - y1) * scalar))] = char


def show():
    output = '\n'.join(''.join(i) for i in screen_buffer)
    print(output)


def clear(char):
    for i in screen_buffer:
        for j in range(screen_width):
            i[j] = char


def transform_vertices(inp, out, scl, pos, rot):
    near_plane = 1 / tan(fov / 2)

    for i in range((len(inp) // 3)):
        o = i * 3

        space_scaled_x = inp[o]     * scl[0]
        space_scaled_y = inp[o + 1] * scl[1]
        space_scaled_z = inp[o + 2] * scl[2]

        # rotation around y axis only
        cosv, sinv = cos(rot), sin(rot)
        space_rotated_x = cosv * space_scaled_x + sinv * space_scaled_z
        space_rotated_z = cosv * space_scaled_z - sinv * space_scaled_x

        space_transformed_x = space_rotated_x + pos[0]
        space_transformed_y = space_scaled_y  + pos[1]
        space_transformed_z = space_rotated_z + pos[2]

        projection_scalar = (near_plane / space_transformed_z)

        screen_projected_x = projection_scalar * space_transformed_x
        screen_projected_y = projection_scalar * space_transformed_y

        out[i * 2]     = screen_projected_x
        out[i * 2 + 1] = screen_projected_y

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

    point_buffer = [0] * ((len(cube_vertices) // 3) * 2)

    cube_position = (0.0, 0.0, 2.5)
    cube_scale    = (1.0, 1.0, 1.0)
    cube_rotation = 0.0

    for frame in range(50):

        cube_rotation += (2 * pi) / 50

        transform_vertices(cube_vertices, point_buffer, cube_scale, cube_position, cube_rotation)

        clear(' ')
        system(CLEAR_COMMAND)

        for i in range(0, len(cube_indices), 2):
            ax, ay = point_buffer[cube_indices[i] * 2]    , point_buffer[cube_indices[i] * 2 + 1]
            bx, by = point_buffer[cube_indices[i + 1] * 2], point_buffer[cube_indices[i + 1] * 2 + 1]
            apx, apy = ((ax + 1.0) / 2) * screen_width, ((ay + 1.0) / 2) * screen_height
            bpx, bpy = ((bx + 1.0) / 2) * screen_width, ((by + 1.0) / 2) * screen_height
            draw_line(int(round(apx)), int(round(apy)), int(round(bpx)), int(round(bpy)), '#')

        show()
        sleep(0.1)

main()

