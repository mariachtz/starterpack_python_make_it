



# Import relevant functions from the module 'drawing'
# Create constant COLOUR for the colour of the drawing
# Create constant PATH for where to save the SVG drawing
# Save radial lines into a file

from drawing import make_drawing_radial_lines
from drawing import make_drawing_cross
from drawing import save_in_file
from drawing import draw_line
COLOUR = "blue"

# Create the SVG content
svg_content = make_drawing_cross(draw_line, COLOUR)

# # Print to check if it looks okay
print(svg_content)

# Save to file
save_in_file("4_creative_art/art.svg", svg_content)


radial_svg = make_drawing_radial_lines(COLOUR)
print(radial_svg)
save_in_file("4_creative_art/radial.svg", radial_svg)
