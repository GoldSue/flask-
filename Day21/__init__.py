
from flask import Flask,request,redirect,session

def auth():
    if request.path.startswith('/static'):
        return
    if request.path == '/login':
        return

    user_info = session.get("user_info")
    if user_info:
        return
    return redirect('/login')

def create_app():
    app = Flask(__name__)
    app.secret_key = 'fdsfdsafdsagsgrewgsgewrgf'

    from .views import account
    from .views import order
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)

    app.before_request(auth)


    return app