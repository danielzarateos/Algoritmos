from flask import Flask, request, make_response, redirect, render_template
#se crea el contendedor del app
app = Flask(__name__)
@app.route('/')
def home():
    user_Ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('ip',user_Ip)
    response.set_cookie('perro','bruno')
    return(response)

#    return f"Hola, tu ip es {user_ip}"
@app.route('/hello')
def helloRoute():
    perro = request.cookies.get('perro')
    ip = request.cookies.get('ip')
    return render_template('hello.html', mascota = perro, userIp = ip)
@app.route('/hey')
def heyRoute():
    return render_template('hey.html')


if __name__ == '__main__':
    app.run()

from flask import Flask, request, make_response, redirect, render_template

# se crea un objeto del tipo app
app = Flask(__name__)

@app.route('/')
def homeRoute():
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    response.set_cookie('ip',user_ip)
    response.set_cookie('gato','Lior Herrera')
    return render_template('home.html')

@app.route('/hello')
def helloRoute():
    gato = request.cookies.get('gato')
    ip = request.cookies.get('ip')
    return render_template('hello.html', 
    mascota = gato, userIp = ip)
@app.route('/hey')
def heyRoute():
    return render_template('hey.html')



if __name__ == '__main__':
    app.run()