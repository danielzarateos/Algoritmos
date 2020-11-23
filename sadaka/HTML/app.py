from flask import Flask, request, make_response, redirect, render_template, url_for

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def homeRoute():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()