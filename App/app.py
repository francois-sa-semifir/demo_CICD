# Importation de Flask et des Blueprints depuis les modules des routes
from flask import Flask
from routes.main_routes import main_bp

# Création d'une application Flask
app = Flask(__name__)

# Enregistrement le blueprint dans l'application Flask
app.register_blueprint(main_bp)

# Exécution de l'application si elle est directement exécutée
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)