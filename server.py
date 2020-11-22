from flask import Flask
from flask import render_template, request, redirect
import csv


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('/index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        category = data["category"]
        radio = data["radio"]
        checkbox = data["checkbox"]
        file = database.write(f'\n{email},{category},{radio},{checkbox}')


def write_to_csv(data):
    with open('database.csv', mode='a') as database2:
        email = data["email"]
        category = data["category"]
        radio = data["radio"]
        checkbox = data["checkbox"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='-', newline='', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,category,radio,checkbox])




@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
        data = request.form.to_dict()
        write_to_csv(data)
        return'/thank-you-page.html'
    except:
        return 'did not save the tab'
    else:
        return 'something went wrong, try again !'