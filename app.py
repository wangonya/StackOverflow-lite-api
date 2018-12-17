from flask import Flask
from resources.auth import auth
from resources.questions import questions

app = Flask(__name__)
app.register_blueprint(auth)
app.register_blueprint(questions)

if __name__ == '__main__':
    app.run()
