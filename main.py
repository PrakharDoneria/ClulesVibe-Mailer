from flask import Flask, request, jsonify
from mailer import Mailer
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

EMAIL = os.getenv('EMAIL')
PASSWORD = os.getenv('PASSWORD')

mail = Mailer(email=EMAIL, password=PASSWORD)
mail.settings(provider=mail.MICROSOFT)

@app.route('/sendMail', methods=['GET'])
def send_email():
    receiver = request.args.get('email')
    subject = request.args.get('subject')
    message = request.args.get('body')

    if not receiver or not subject or not message:
        return jsonify({'error': 'Email, subject, and body are required'}), 400

    message = message.replace('\\n', '\n')

    mail.send(receiver=receiver, subject=subject, message=message)

    if mail.status:
        return jsonify({'status': 'success'}), 200
    else:
        return jsonify({'status': 'failed'}), 500

if __name__ == '__main__':
    app.run(debug=True)
