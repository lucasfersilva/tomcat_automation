from flask import Flask, request, render_template
import openai

openai.api_key = 'your-openai-api-key'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    response = openai.Completion.create(engine="text-davinci-002", prompt=userText, max_tokens=150)
    return str(response.choices[0].text.strip())

if __name__ == "__main__":
    app.run()
