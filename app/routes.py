"""
Defines the routes for the application.
"""

from flask import render_template, request, jsonify, current_app
import os
import tempfile
from .wordcloud_generator import generate_wordcloud_image

@current_app.route('/')
def index():
    """
    Renders the index page.
    """
    return render_template('index.html')

@current_app.route('/generate_wordcloud', methods=['POST'])
def generate_wordcloud_route():
    """
    Generates a word cloud from the provided text.
    """
    text = request.form.get('text')
    colormap = request.form.get('colormap', 'viridis')
    background_color = request.form.get('background_color', 'white')
    font_file = request.files.get('font_file')

    font_path = None
    if font_file and font_file.filename != '':
        # Save the uploaded font file temporarily
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.ttf') as temp_font:
                font_file.save(temp_font.name)
                font_path = temp_font.name
        except Exception as e:
            current_app.logger.error(f"Error saving font file: {e}")
            return jsonify({'error': 'Failed to process font file.'}), 500

    if not text:
        # Clean up temporary font file if it was uploaded
        if font_path and os.path.exists(font_path):
            os.remove(font_path)
        return jsonify({'error': 'No text provided'}), 400

    try:
        img_str = generate_wordcloud_image(text, colormap=colormap, background_color=background_color, font_path=font_path)
        return jsonify({'wordcloud': img_str})
    except Exception as e:
        current_app.logger.error(f"Error generating word cloud: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500
    finally:
        # Clean up temporary font file
        if font_path and os.path.exists(font_path):
            os.remove(font_path)
