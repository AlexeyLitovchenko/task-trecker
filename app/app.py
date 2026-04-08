from flask import Flask, jsonify
import socket
import os
import time

app = Flask(__name__)

STUDENT = os.getenv("STUDENT_NAME", "Litovchenko")
START_TIME = time.time()

@app.route("/", methods=["GET"])
def index():
    # выполняет GET запрос по endpoint '/', возвращая json с названием сервиса, наименованием хоста, фамилией
    return jsonify({
        "service": "task-tracker",
        "hostname": socket.gethostname(),
        "student": STUDENT
    })

@app.route("/health", methods=["GET"])
def health():
    # выполняет GET запрос по endpoint '/health', возвращая json со статус 'ok'
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    # host=0.0.0.0 + фвно указываем порт приложения 8080
    app.run(host="0.0.0.0", port=8080)