document.getElementById('text-input').addEventListener('input', function() {
    const text = this.value;
    if (text.trim() === '') {
        document.getElementById('wordcloud-container').innerHTML = '';
        return;
    }

    fetch('/generate_wordcloud', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
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
});
