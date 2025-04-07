"""Collection of SVG drawing functions"""

from random import choice, randrange, sample
import nltk
from nltk.tokenize import sent_tokenize

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


nltk.download('punkt')
nltk.download('punkt_tab')

def make_drawing_abstract_sentences():

    with open('book.txt', 'r', encoding='utf-8', errors='ignore') as file:
        text = file.read()

    # Split text into a list of sentences
    sentence_list = sent_tokenize(text)

    # Building the SVG drawing
    svg = '<svg viewBox="0 0 2000 3000" width="2000" height="3000" xmlns="http://www.w3.org/2000/svg">\n'

    # Initialize the variables
    x, y = 1000, 1500 
    turn_counter = 0 
    path_data = f'M {x} {y} '  

 
    for sentence in sentence_list:

        # Count the number of words in the sentence
        number_words = len(sentence.replace('\n', ' ').split(' '))

        # Move the path in the correct direction based on the turn_counter
        if turn_counter == 0:  
            x += number_words
        elif turn_counter == 1:  
            y += number_words
        elif turn_counter == 2:  
            x -= number_words
        else:  
            y -= number_words

        # Add line to the SVG path
        path_data += f'L {x} {y} '

        # Increment the turn_counter
        turn_counter += 1
        turn_counter %= 4  # Keep it between 0 and 3

    # Close the path and the SVG drawing
    svg += f'<path d="{path_data}" stroke="black" fill="none" />\n'
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



