from flask import Flask, jsonify
import threading
from activos_adjuntos.bot_circleads import login, iniciar, detener, driver

app = Flask(__name__)

@app.route("/iniciar", methods=["POST"])
def iniciar_bot():
    try:
        thread = threading.Thread(target=iniciar)
        thread.start()
        return jsonify({"status": "Bot iniciado"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/detener", methods=["POST"])
def detener_bot():
    try:
        detener()
        return jsonify({"status": "Bot detenido"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/estado", methods=["GET"])
def estado():
    try:
        return jsonify({"activo": hasattr(driver, "service") and driver.service.process})
    except:
        return jsonify({"activo": False})

if __name__ == "__main__":
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
