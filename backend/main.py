from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_cursor

app = Flask(__name__)
CORS(app)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        cursor = get_cursor()
        cursor.execute("SELECT * FROM Users WHERE username=? AND password=?", (username, password))
        result = cursor.fetchone()

        if result:
            return jsonify({'status': 'success'})
        else:
            return jsonify({'status': 'fail', 'message': 'Invalid credentials'})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({'status': 'error', 'message': 'Backend error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
