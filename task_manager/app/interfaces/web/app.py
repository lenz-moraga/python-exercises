from flask import Flask

app = Flask(__name__)
app.secret_key = 'una_clave_muy_segura_que_tú_elijas'

from app.interfaces.web.routes import register_routes
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
