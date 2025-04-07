"""Collection of SVG drawing functions"""

def draw_line(x, y, x2, y2, colour):
    return f'<line x1="{x}" y1="{y}" x2="{x2}" y2="{y2}" stroke="{colour}" />\n'




def make_drawing_radial_lines(colour= "black", width=100, height=100, granularity=5):
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

def save_in_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)

def make_drawing_cross(draw_line_function, colour):
    svg = '<svg viewBox="0 0 100 100" width="100" height="100" xmlns="http://www.w3.org/2000/svg">\n'
    svg += draw_line_function(10, 10, 90, 90, colour)
    svg += draw_line_function(10, 90, 90, 10, colour)
    svg += '</svg>'
    return svg
