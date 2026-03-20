from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "TOKEN_HASH8=9238838b\n"

if __name__ == '__main__':
    # Явно отключаем многопоточность для стабильности в контейнере
    app.run(host='0.0.0.0', port=8080, threaded=False)
