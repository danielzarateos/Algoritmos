from flask import Flask, request, make_response, redirect, render_template, url_for

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def homeRoute():
    return render_template('home.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')

@app.route('/pacientes')
def pacientesesRoute():
    return render_template('pacientes.html')
@app.route('/doctors')
def doctorsRoute():
    return render_template('doctors.html')
@app.route('/conocenos')
def abaoutRoute():
    return render_template('conocenos.html')
@app.route('/contact')
def contactRoute():
    return render_template('contact.html')
@app.route('/curioso')
def profegraciasportodoRoute():
    return render_template('curioso.html')

if __name__ == '__main__':
    app.run()