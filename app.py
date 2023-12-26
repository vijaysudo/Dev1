from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            number = float(request.form['number'])
            result = number ** 2
        except ValueError:
            result = 'Please enter a valid number.'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    
