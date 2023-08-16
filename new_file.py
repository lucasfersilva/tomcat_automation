from flask import Flask, render_template
import os

app = Flask(__name__)

def search_files(path):
    file_dict = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_dict[file] = os.path.join(root, file)
    return file_dict

@app.route('/')
def home():
    path = "C:/"
    file_dict = search_files(path)
    return render_template('index.html', file_dict=file_dict)

if __name__ == "__main__":
    app.run(debug=True)
