const textInput = document.getElementById('text-input');
const colormapSelect = document.getElementById('colormap-select');
const backgroundColorInput = document.getElementById('background-color-input');
const fontFileInput = document.getElementById('font-file-input');
const stopwordsInput = document.getElementById('stopwords-input');

function generateWordCloud() {
    const text = textInput.value;
    if (text.trim() === '') {
        document.getElementById('wordcloud-container').innerHTML = '';
        return;
    }

    const formData = new FormData();
    formData.append('text', text);
    formData.append('colormap', colormapSelect.value);
    formData.append('background_color', backgroundColorInput.value);

    if (fontFileInput.files.length > 0) {
        formData.append('font_file', fontFileInput.files[0]);
    }
    formData.append('custom_stopwords', stopwordsInput.value);

    fetch('/generate_wordcloud', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.wordcloud) {
            const img = document.createElement('img');
            img.id = 'wordcloud';
            img.src = 'data:image/png;base64,' + data.wordcloud;
            document.getElementById('wordcloud-container').innerHTML = '';
            document.getElementById('wordcloud-container').appendChild(img);
        }
    });
}

textInput.addEventListener('input', generateWordCloud);
colormapSelect.addEventListener('change', generateWordCloud);
backgroundColorInput.addEventListener('change', generateWordCloud);
fontFileInput.addEventListener('change', generateWordCloud);
stopwordsInput.addEventListener('input', generateWordCloud);
