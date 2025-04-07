# Import relevant functions from the module 'drawing'
from drawing import make_drawing_radial_lines
from drawing_for_step_5 import make_drawing_random_radial_lines, make_drawing_abstract_sentences

# Import the object Flask from the flask module
from flask import Flask, request

# Create constant COLOUR
COLOUR = "purple"

# Create constant PATH 
PATH = "4_creative_art/drawing.svg"

# Create a webserver object called 'Generative Art'
server = Flask('Generative Art')

# Define an HTTP route /radial to serve the radial lines drawing
@server.route('/radial')

# Define the function 'serve_radial_lines()' and connect it to the route /radial
def serve_radial_lines():
    """
    Make drawing radial lines
    """

    return make_drawing_radial_lines(colour = COLOUR)

# Define an HTTP route /radial/<width>/<height> to serve custom radial lines drawing
@server.route('/radial/<width>/<height>')

# Define the function 'serve_custom_radial_lines()' and connect it to the route /radial/<width>/<height>
def serve_custom_radial_lines(width, height):
    """
    Make drawing radial lines with specified width and height
    colour (optional, default="black") -- Query parameter
    granularity (optional, default="5") -- Query parameter
    """

    width = int(width)
    height = int(height)

    colour = request.args.get('colour', default="black", type=str)  
    granularity = request.args.get('granularity', default=5, type=int) 

    return make_drawing_radial_lines(colour=colour, width=width, height=height, granularity=granularity)

# Define an HTTP route /random to serve random radial lines drawing
@server.route('/random')

# Define the function 'serve_random_radial_lines()' and connect it to the route /random
def serve_random_radial_lines():
    """
    Mamke random radial lines
    """
    return make_drawing_random_radial_lines()

# Define an HTTP route /sentences to serve random radial lines drawing
@server.route('/sentences')


# Define the function 'serve_abstract_sentences()' and connect it to the route /sentences
def serve_abstract_sentences():
    """
    Make abstract sentence drawing
    """
    return make_drawing_abstract_sentences()

# Start the webserver
server.run('0.0.0.0')
