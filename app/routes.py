"""
Defines the routes for the application.
"""

from flask import render_template, request, jsonify, current_app
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
    text = request.json.get('text')
    colormap = request.json.get('colormap', 'viridis')
    background_color = request.json.get('background_color', 'white')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        img_str = generate_wordcloud_image(text, colormap=colormap, background_color=background_color)
        return jsonify({'wordcloud': img_str})
    except Exception as e:
        current_app.logger.error(f"Error generating word cloud: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500
