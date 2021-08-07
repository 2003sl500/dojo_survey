from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "29439238"

@app.route('/')
def index():
    return render_template("/index.html")

@app.route('/process', methods=['POST'])
def process():
    session['form'] = request.form
    print(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template("/result.html")

@app.route('/return', methods = ['POST'])
def return_home():
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)