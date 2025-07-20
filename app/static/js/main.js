const textInput = document.getElementById('text-input');
const colormapSelect = document.getElementById('colormap-select');
const backgroundColorInput = document.getElementById('background-color-input');

function generateWordCloud() {
    const text = textInput.value;
    if (text.trim() === '') {
        document.getElementById('wordcloud-container').innerHTML = '';
        return;
    }

    const colormap = colormapSelect.value;
    const backgroundColor = backgroundColorInput.value;

    fetch('/generate_wordcloud', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 
            text: text,
            colormap: colormap,
            background_color: backgroundColor
        })
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