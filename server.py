from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name + '.html')

@app.route('/submit_form', method=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    print(data)
    return 'form submitted'
  else:
    return 'something went wrong'