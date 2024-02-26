from flask import Flask, render_template
import requests

app = Flask(__name__)

def generate():
    api = 'https://api.adviceslip.com/advice'
    data = requests.get(api)
    if data.status_code == 200:
        content = data.json()['slip']
        return content

@app.route('/')
def index():
    advice_content = generate()  # Call the generate function to get the advice content
    return render_template('index.html', id=advice_content['id'], advice=advice_content['advice'])

