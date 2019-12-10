from flask import Flask, render_template, request
import json

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/app.py')
def whatever():
    with open("\\Users\Mohammad Khwaja\.PyCharmCE2019.2\config\scratches\json_destination\watchdog_file.json","w") as json_file:
        json.dump(request.args, json_file)
    return request.args
if __name__ == '__main__':
    app.run(debug=True)