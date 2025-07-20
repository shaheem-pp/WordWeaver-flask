"""
Defines the routes for the application.
"""

from flask import render_template, request, jsonify, current_app
import os
import tempfile
import requests
from bs4 import BeautifulSoup
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
    text_input = request.form.get('text')
    url_input = request.form.get('url')
    colormap = request.form.get('colormap', 'viridis')
    background_color = request.form.get('background_color', 'white')
    font_file = request.files.get('font_file')
    custom_stopwords = request.form.get('custom_stopwords')
    mask_file = request.files.get('mask_file')

    text = ""
    if url_input:
        try:
            response = requests.get(url_input)
            response.raise_for_status()  # Raise an exception for HTTP errors
            soup = BeautifulSoup(response.text, 'html.parser')
            text = soup.get_text()
        except requests.exceptions.RequestException as e:
            current_app.logger.error(f"Error fetching URL {url_input}: {e}")
            return jsonify({'error': f'Failed to fetch content from URL: {e}'}), 400
        except Exception as e:
            current_app.logger.error(f"Error parsing URL content {url_input}: {e}")
            return jsonify({'error': 'Failed to parse content from URL.'}), 400
    elif text_input:
        text = text_input

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

    mask_path = None
    if mask_file and mask_file.filename != '':
        # Save the uploaded mask file temporarily
        try:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.png') as temp_mask: # Assuming PNG for now, can be more flexible
                mask_file.save(temp_mask.name)
                mask_path = temp_mask.name
        except Exception as e:
            current_app.logger.error(f"Error saving mask file: {e}")
            return jsonify({'error': 'Failed to process mask file.'}), 500

    if not text:
        # Clean up temporary files if they were uploaded
        if font_path and os.path.exists(font_path):
            os.remove(font_path)
        if mask_path and os.path.exists(mask_path):
            os.remove(mask_path)
        return jsonify({'error': 'No text provided'}), 400

    try:
        img_str = generate_wordcloud_image(text, colormap=colormap, background_color=background_color, font_path=font_path, custom_stopwords=custom_stopwords, mask_path=mask_path)
        return jsonify({'wordcloud': img_str})
    except Exception as e:
        current_app.logger.error(f"Error generating word cloud: {e}")
        return jsonify({'error': 'An unexpected error occurred.'}), 500
    finally:
        # Clean up temporary files
        if font_path and os.path.exists(font_path):
            os.remove(font_path)
        if mask_path and os.path.exists(mask_path):
            os.remove(mask_path)
