from flask import Flask, request, make_response, redirect, render_template, url_for

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def homeRoute():
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/services')
def servicesRoute():
    return render_template('services.html')
@app.route('/doctors')
def doctorsRoute():
    return render_template('doctors.html')
@app.route('/doctors')
def abaoutRoute():
    return render_template('abaout.html')


if __name__ == '__main__':
    app.run()