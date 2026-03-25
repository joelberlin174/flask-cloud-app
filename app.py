from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os

app = Flask(__name__)

BASE_FOLDER = 'storage'
app.config['BASE_FOLDER'] = BASE_FOLDER

# create base folder
if not os.path.exists(BASE_FOLDER):
    os.makedirs(BASE_FOLDER)

@app.route('/')
def home():
    folders = os.listdir(BASE_FOLDER)
    return render_template('index.html', folders=folders)

@app.route('/create_folder', methods=['POST'])
def create_folder():
    folder_name = request.form['folder']
    path = os.path.join(BASE_FOLDER, folder_name)

    if not os.path.exists(path):
        os.makedirs(path)

    return redirect(url_for('home'))

@app.route('/folder/<name>')
def open_folder(name):
    path = os.path.join(BASE_FOLDER, name)
    files = os.listdir(path)
    return render_template('folder.html', folder=name, files=files)

@app.route('/upload/<folder>', methods=['POST'])
def upload(folder):
    file = request.files['file']
    path = os.path.join(BASE_FOLDER, folder)

    if file:
        file.save(os.path.join(path, file.filename))

    return redirect(url_for('open_folder', name=folder))

@app.route('/download/<folder>/<filename>')
def download(folder, filename):
    return send_from_directory(os.path.join(BASE_FOLDER, folder), filename)

if __name__ == "__main__":
    app.run()
