from io import BytesIO

from PIL import Image, ImageDraw
from flask import Flask, send_file

application = Flask(__name__)

@application.route('/<dimensions>')
def index(dimensions):
    # Setup
    dimensions = tuple(map(int, dimensions.split('x')))
    color = (124, 127, 129)

    # IO stream
    content = BytesIO()

    # Generate image
    image = Image.new('RGB', dimensions, color)

    # draw text
    draw = ImageDraw.Draw(image)
    text = '%s x %s' % dimensions
    text_width, text_height = draw.textsize(text)

    if text_width < dimensions[0] and text_height < dimensions[1]:
        text_left = (dimensions[0] - text_width) // 2
        text_top = (dimensions[1] - text_height) // 2
        draw.text((text_left, text_top), text, fill=(255, 255, 255))

    # Save image to bytes stream
    image.save(content, 'PNG')
    content.seek(0) 

    return send_file(content, mimetype='image/png', attachment_filename='image.png')