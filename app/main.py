from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health_check():
    return jsonify({"status": "OK"})

@app.route('/')
def hello_world():
    return jsonify({"message": "Hello! This is a sample CI/CD application"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
