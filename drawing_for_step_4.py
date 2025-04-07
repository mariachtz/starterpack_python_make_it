"""Collection of SVG drawing functions"""

from random import choice, randrange, sample


def draw_line(x, y, x2, y2, colour):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{colour}" />\n'




def make_drawing_radial_lines(colour="black", width=100, height=100, granularity=5):
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    x = granularity                         # Left with margin
    y = granularity                         # Top with margin
    x2 = width - granularity                # Right with margin
    y2 = height - granularity               # Bottom with margin

    # Vertical movement -  y and y2
    for i in range(0, height, granularity):
        svg += draw_line(x, y + i, x2, y2 - i, colour)

    # Horizontal movement - x and x2
    for i in range(0, width, granularity):
        svg += draw_line(x + i, y, x2 - i, y2, colour)

    svg += '</svg>'
    return svg


def generate_random_hexadecimal_colour():
    hexadecimal_characters = '0123456789ABCDEF'
    random_value_list = sample(hexadecimal_characters, 6)
    return '#' + ''.join(random_value_list)


def make_drawing_random_radial_lines(colour="black", width=100, height=100, granularity=5):
    svg = f'<svg viewBox="0 0 {width} {height}" width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">\n'

    x = granularity
    y = granularity
    x2 = width - granularity
    y2 = height - granularity

    # Vertical movement - y and y2
    for i in range(0, height, granularity):
        if choice([True, False]):
            offset1 = randrange(0, width // 2)
            offset2 = randrange(0, width // 2)
            colour = generate_random_hexadecimal_colour()
            svg += draw_line(x, y + i + offset1, x2, y2 - i - offset2, colour)

    # Horizontal movement - x and x2
    for i in range(0, width, granularity):
        if choice([True, False]):
            offset1 = randrange(0, height // 2)
            offset2 = randrange(0, height // 2)
            colour = generate_random_hexadecimal_colour()
            svg += draw_line(x + i + offset1, y, x2 - i - offset2, y2, colour)

    svg += '</svg>'
    return svg


def save_in_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)




def make_drawing_cross(draw_line_function, colour):
    svg = '<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">\n'
    svg += draw_line_function(10, 10, 90, 90, colour)
    svg += draw_line_function(10, 90, 90, 10, colour)
    svg += '</svg>'
    return svg
