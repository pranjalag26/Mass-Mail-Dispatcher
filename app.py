from flask import Flask, render_template, request
import json
import os
from email_read import get_csv_data
from mail import isValid
from send_mail import send_email


app = Flask(__name__)

# List to store valid emails
valid = []
# List to store invalid emails
invalid = []
# Name of the uploaded file
filename = ""

# Route
@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        f = request.files['file']
        if not os.path.isdir('./uploads'):
            os.mkdir('./uploads')
        path = os.path.join('./uploads', f.filename)
        f.save(path)
        emails = get_csv_data(f.filename)
        filename = f.filename
        valid.clear()
        invalid.clear()
        for i in emails:
            if isValid(i):
                valid.append(i)
            else:
                invalid.append(i)
        print(valid, len(valid))
        print("\n")
        print(invalid, len(invalid))
        return render_template('index.html')
    filename = ""
    return render_template('upload.html')


@app.route("/valid", methods=['GET'])
def val():
    return render_template('show_email_valid.html', your_list=valid, leng=len(valid))


@app.route("/invalid", methods=['GET'])
def inval():
    return render_template('show_email_invalid.html', your_list=invalid, leng=len(invalid))


@app.route("/send", methods=['GET'])
def send():
    send_email(valid)
    return render_template('send.html')


if __name__ == "__main__":
    app.run(debug=True)
