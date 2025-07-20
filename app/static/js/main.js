const textInput = document.getElementById('text-input');
const urlInput = document.getElementById('url-input');
const colormapSelect = document.getElementById('colormap-select');
const backgroundColorInput = document.getElementById('background-color-input');
const fontFileInput = document.getElementById('font-file-input');
const stopwordsInput = document.getElementById('stopwords-input');
const maskFileInput = document.getElementById('mask-file-input');
const downloadWordcloudBtn = document.getElementById('download-wordcloud');

function generateWordCloud() {
    const text = textInput.value;
    const url = urlInput.value;

    if (text.trim() === '' && url.trim() === '') {
        document.getElementById('wordcloud-container').innerHTML = '';
        downloadWordcloudBtn.style.display = 'none'; // Hide download button
        return;
    }

    const formData = new FormData();
    if (url.trim() !== '') {
        formData.append('url', url);
    } else {
        formData.append('text', text);
    }
    formData.append('colormap', colormapSelect.value);
    formData.append('background_color', backgroundColorInput.value);

    if (fontFileInput.files.length > 0) {
        formData.append('font_file', fontFileInput.files[0]);
    }
    formData.append('custom_stopwords', stopwordsInput.value);

    if (maskFileInput.files.length > 0) {
        formData.append('mask_file', maskFileInput.files[0]);
    }

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
            downloadWordcloudBtn.href = 'data:image/png;base64,' + data.wordcloud;
            downloadWordcloudBtn.style.display = 'block'; // Show download button
        } else if (data.error) {
            document.getElementById('wordcloud-container').innerHTML = `<p class="text-danger">Error: ${data.error}</p>`;
            downloadWordcloudBtn.style.display = 'none'; // Hide download button on error
        }
    });
}

textInput.addEventListener('input', generateWordCloud);
urlInput.addEventListener('input', generateWordCloud);
colormapSelect.addEventListener('change', generateWordCloud);
backgroundColorInput.addEventListener('change', generateWordCloud);
fontFileInput.addEventListener('change', generateWordCloud);
stopwordsInput.addEventListener('input', generateWordCloud);
maskFileInput.addEventListener('change', generateWordCloud);
