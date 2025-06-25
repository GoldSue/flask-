from flask import Flask, request, redirect, session


def auth():
    if request.path.startswith('/static'):
        return
    if request.path == '/login':
        return

    user_info = session.get("user_info")
    if user_info:
        return
    return redirect('/login')


def my_context_processor():
    user_info = session.get("user_info")
    real_name = user_info['real_name']
    return real_name


def create_app():
    app = Flask(__name__)
    app.secret_key = 'your-secret-key'  # 生产环境请改为安全密钥

    from .views import account
    from .views import order
    app.register_blueprint(account.ac)
    app.register_blueprint(order.od)
    app.template_global()(my_context_processor)

    app.before_request(auth)

    return app
