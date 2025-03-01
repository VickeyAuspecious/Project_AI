
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question')
    
    # Call the local Ollama LLM model
    response = requests.post('http://localhost:8000/ask', json={'question': question})
    answer = response.json().get('answer')
    
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
