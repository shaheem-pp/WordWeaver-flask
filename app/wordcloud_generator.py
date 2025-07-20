"""
This module contains the logic for generating word clouds.
"""

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import numpy as np
from PIL import Image
import base64
from io import BytesIO

def generate_wordcloud_image(text, colormap='viridis', background_color='white', font_path=None, custom_stopwords=None, mask_path=None):
    """
    Generates a word cloud image from the given text.

    Args:
        text (str): The text to generate the word cloud from.
        colormap (str): The colormap for the word cloud.
        background_color (str): The background color of the word cloud.
        font_path (str, optional): The path to the font file. Defaults to None.
        custom_stopwords (str, optional): A comma-separated string of custom stopwords. Defaults to None.
        mask_path (str, optional): The path to the mask image file. Defaults to None.

    Returns:
        str: A base64 encoded string representing the word cloud image.
    """
    stopwords = set(STOPWORDS)
    if custom_stopwords:
        stopwords.update([word.strip() for word in custom_stopwords.split(',')])

    mask = None
    mask_img = None
    if mask_path:
        mask_img = Image.open(mask_path).convert('RGB')
        mask = np.array(mask_img)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color=background_color,
        colormap=colormap if not mask_img else None,  # Use colormap only if no mask image
        font_path=font_path,
        stopwords=stopwords,
        mask=mask
    ).generate(text)

    # If mask image is provided, use its colors
    if mask_img is not None:
        image_colors = ImageColorGenerator(np.array(mask_img))
        wordcloud = wordcloud.recolor(color_func=image_colors)

    img_buffer = BytesIO()
    wordcloud.to_image().save(img_buffer, format='PNG')
    return base64.b64encode(img_buffer.getvalue()).decode('utf-8')
