from flask import Flask, render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/fabian')
def fabian():
    return 'Hi Fabian!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    
