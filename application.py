from flask import Flask, request, jsonify

application = Flask(__name__)

@application.route('/', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy"}), 200

@application.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    if not text:
        return jsonify({"error": "Bad Request"}), 400
    return jsonify({"message": f"You submitted: {text}"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000) 