# WordWeaver

WordWeaver is a dynamic web application that allows you to generate beautiful and highly customizable word clouds from text or web pages. It's built with Flask and the `wordcloud` library, featuring a live-updating interface for a seamless user experience.

![WordWeaver Screenshot](placeholder.png) <!-- It's recommended to replace this with an actual screenshot of the application -->

## ✨ Features

WordWeaver comes packed with features to make your word cloud generation process flexible and creative:

*   **Live Generation**: The word cloud updates in real-time as you type or change settings.
*   **Multiple Text Sources**:
    *   **Direct Text Input**: Paste your text directly into the application.
    *   **URL Scraper**: Provide a URL, and WordWeaver will automatically scrape the text content from the page.
*   **Extensive Customization**:
    *   **Color Schemes**: Choose from a variety of built-in color maps.
    *   **Background Color**: Select any background color using a color picker.
    *   **Custom Fonts**: Upload your own `.ttf` font files for a unique look.
    *   **Image Masking**: Upload an image (PNG, JPG) to shape your word cloud and even color it using the image's palette.
*   **Stop Words Control**:
    *   **Custom Stop Words**: Specify additional words to be excluded from the word cloud.
    *   **Language Presets**: Select default stop words for languages like English, French, German, and Spanish.
*   **Download**: Save your final creation as a high-quality PNG image with a single click.
*   **Fully Responsive**: The user interface is designed to work flawlessly on both desktop and mobile devices.

## 🛠️ Tech Stack

*   **Backend**: Flask, wordcloud, Pillow, BeautifulSoup4, Requests
*   **Frontend**: Vanilla JavaScript, Bootstrap 5, HTML5, CSS3
*   **Deployment**: Can be deployed on any platform that supports Python WSGI applications (e.g., Gunicorn, Heroku, Vercel).

## 🚀 Getting Started

Follow these instructions to get a local copy of WordWeaver up and running.

### Prerequisites

*   Python 3.8+
*   A virtual environment tool (`venv`)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/WordWeaver.git
    cd WordWeaver
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install the dependencies from `requirements.txt`:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the application:**
    ```bash
    python run.py
    ```

5.  Open your web browser and navigate to `http://127.0.0.1:5000`.

## 📂 Project Structure

```
WordWeaver/
├── app/
│   ├── static/
│   │   ├── css/style.css         # Main stylesheet
│   │   └── js/main.js            # Frontend JavaScript logic
│   ├── templates/
│   │   └── index.html            # Main HTML template
│   ├── __init__.py               # Flask app factory
│   ├── routes.py                 # Application routes and view logic
│   └── wordcloud_generator.py    # Core word cloud generation logic
├── config.py                     # Application configuration settings
├── requirements.txt              # Python package dependencies
└── run.py                        # Application entry point
```

## 📈 Future Enhancements

While WordWeaver is already a powerful tool, here are some potential features for the future:

*   **Social Sharing**: Add buttons to directly share the generated word cloud on social media platforms.
*   **User Accounts**: Allow users to create accounts to save their word clouds and custom settings.
*   **Public API**: Expose an API for developers to integrate word cloud generation into their own applications.
*   **More Export Formats**: Support for downloading in formats like JPEG, SVG, or PDF.

## 🤝 Contributing

Contributions are welcome! If you have ideas for new features or improvements, feel free to open an issue or submit a pull request.

1.  Fork the Project
2.  Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the Branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 📄 License

This project is open-source and available to everyone.

---

_This README was generated with assistance from GitHub Copilot._

