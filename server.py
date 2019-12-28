from bottle import route, run, template, request, Bottle

app = Bottle(__name__)

@app.route('/')
def root():
    return "Hello from Root!!"

@app.route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

