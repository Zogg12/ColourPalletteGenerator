"""
This module sets up a Flask web application to upload an image,
extract the top colors from that image, and display them to the user.
The application provides a simple interface for users to interact with
image color extraction functionality.
"""

from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from color_processing import extract_top_colors

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Define upload folder


# Home route: display upload form
@app.route('/')
def index():
    """
    Render the home page where users can upload an image for color extraction.

    :return: Rendered HTML template for the index page.
    """
    return render_template('index.html')


# Route to handle image uploads
@app.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle the uploaded image file, extract the top 10 colors, and render the results.

    This function checks if the uploaded file is present and valid,
    saves it to the designated upload folder, processes the image to
    extract colors, and then deletes the image file after processing.

    :return: Rendered HTML template for the results page with the extracted colors.
    """
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        # Extract top 10 colors
        top_colors = extract_top_colors(file_path)

        # Remove the file after processing
        os.remove(file_path)

        return render_template('result.html', colors=top_colors)


if __name__ == "__main__":
    app.run(debug=True)
