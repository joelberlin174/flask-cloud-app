from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

history = []   # shared history for all users

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add():
    global history
    data = request.json
    history.append(data['calc'])

    # limit history to last 10
    history = history[-10:]
    return jsonify({"status": "ok"})

@app.route('/history')
def get_history():
    return jsonify(history)

if __name__ == "__main__":
    app.run()
