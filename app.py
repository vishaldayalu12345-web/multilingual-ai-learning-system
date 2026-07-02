from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    language_codes = {
        "English": "en",
        "Kannada": "kn",
        "Telugu": "te",
        "Marathi": "mr",
        "Hindi": "hi",
        "Punjabi": "pa"
    }

    if request.method == 'POST':

        text = request.form['text']
        source_language = request.form['source_language']
        target_language = request.form['target_language']

        # Create translator using language codes
        translator = GoogleTranslator(
            source=language_codes[source_language],
            target=language_codes[target_language]
        )

        # Translate the text
        translated_text = translator.translate(text)

        # Send all data to HTML
        return render_template(
            'index.html',
            text=text,
            source_language=source_language,
            target_language=target_language,
            translated_text=translated_text
        )

    # First time opening the page
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)