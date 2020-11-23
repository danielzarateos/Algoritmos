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
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')
@app.route('/hello')
def helloRoute():
    perro = request.cookies.get('perro')
    ip = request.cookies.get('ip')
    return render_template('hello.html', mascota = perro, userIp = ip)
@app.route('/cosas')
def cosasRoute():
    return render_template('cosas.html')
@app.route('/personas')
def personasRoute():
    return render_template('personas.html')


if __name__ == '__main__':
    app.run()