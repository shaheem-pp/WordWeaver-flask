# WordWeaver

WordWeaver is a simple web application that generates word clouds from user-provided text. It's built with Flask and WordCloud.

## Project Structure

```
/Users/shaheem/Developer/Projects/WordWeaver/
├───app/
│   ├───__init__.py
│   ├───routes.py
│   ├───wordcloud_generator.py
│   ├───static/
│   │   ├───css/
│   │   │   └───style.css
│   │   └───js/
│   │       └───main.js
│   └───templates/
│       └───index.html
├───config.py
├───requirements.txt
└───run.py
```

## Getting Started

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/WordWeaver.git
    ```

2.  **Create a virtual environment and activate it:**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**

    ```bash
    python run.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## Potential Future Features

*   **Customization:**
    *   Allow users to customize the word cloud's colors, font, and shape.
    *   Add a color picker to choose the background color.
    *   Allow users to upload their own fonts.
*   **Stop Words:**
    *   Allow users to provide a list of stop words to exclude from the word cloud.
    *   Provide a default list of stop words for common languages.
*   **Image Upload:**
    *   Allow users to upload an image to use as a mask for the word cloud.
*   **URL Input:**
    *   Allow users to provide a URL to a web page, and the application will scrape the text from the page to generate the word cloud.
*   **Save and Share:**
    *   Allow users to download the word cloud as an image file (e.g., PNG, JPEG).
    *   Allow users to share the word cloud on social media.
*   **User Accounts:**
    *   Add user accounts to allow users to save their word clouds and settings.
*   **API:**
    *   Create an API to allow other applications to generate word clouds using the WordWeaver service.
