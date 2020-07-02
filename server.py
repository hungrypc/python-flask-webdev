from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
  return render_template(page_name + '.html')

def write_to_file(data):
  with open('db.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write("\n" + email + "\n" + subject + "\n" + message + "\n")


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
  if request.method == 'POST':
    data = request.form.to_dict()
    write_to_file(data)
    return redirect('/thanks')
  else:
    return 'something went wrong'