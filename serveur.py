from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

# Remplacez 'YOUR_OPENAI_API_KEY' par votre clé API
api_key = 'sk-proj-BCtNALBJdUhNjwA2XKPoT3BlbkFJ14y9f2uLvjfWYGvLCL2r'
os.environ["OPENAI_API_KEY"] = api_key
openai.api_key = api_key

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    messages = data.get('messages', [])
    
    chat_response = openai.chat.completions.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        temperature=0.9,
        max_tokens=150,
    )
    
    response_message = chat_response.choices[0].message.content
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
