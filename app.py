from flask import Flask, render_template, request, jsonify
from ciphers import caesar_cipher, vigenere_cipher, XOR_cipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.get_json()
    cipher = data.get('cipher')
    key = data.get('key', '')
    plaintext = data.get('plaintext', '')

    try:
        if cipher == 'caesar':
            result = caesar_cipher(plaintext, int(key))
        elif cipher == 'vigenere':
            result = vigenere_cipher(plaintext, key)
        elif cipher == 'xor':
            if not key:
                return jsonify({'error': 'Key required'}), 400
            result = XOR_cipher(plaintext, key)
        else:
            return jsonify({'error': 'Unknown cipher'}), 400
        return jsonify({'ciphertext': result})
    except ValueError:
        return jsonify({'error': 'Caesar key must be an integer'}), 400

if __name__ == '__main__':
    app.run(debug=True)