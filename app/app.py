from flask import Flask, jsonify
import os
import logging

app = Flask(name)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(name)

@app.route('/')
def home():
return jsonify({
"message": "Cofre Digital Online!",
"environment": os.getenv('ENVIRONMENT', 'unknown'),
"version": os.getenv('APP_VERSION', '1.0.0')
})

@app.route('/database')
def database_info():
db_host = os.getenv('DB_HOST', 'localhost')
db_user = os.getenv('DB_USER', 'user')
db_password = os.getenv('DB_PASSWORD', 'SENHA_NAO_CONFIGURADA')
