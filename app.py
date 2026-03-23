from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

result = ""   # shared for all users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update', methods=['POST'])
def update():
    global result
    data = request.json
    result = data['value']
    return jsonify({"status": "ok"})

@app.route('/get')
def get():
    return jsonify({"value": result})

if __name__ == "__main__":
    app.run()
