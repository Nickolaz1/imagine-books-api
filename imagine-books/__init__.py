import os
from flask import Flask

def create_app(test_config = None):
    # criar e configurar o app
    app = Flask(__name__, instance_relative_config = True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE = os.path.join(app.instance_path, 'imagine-books')
    )

    if test_config is None:
        # carregar as configurações da instância, caso exista, quando não estiver testando
        app.config.from_pyfile('config.py', silent=True)
    else:
        # carregar as configurações de teste
        app.config.from_mapping(test_config)

    # verificar se a pasta da instância existe
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.get("/")
    def index():
        return 'hello'

    @app.route("/produtos")
    def produtos():
        return 'produtos'

    return app
