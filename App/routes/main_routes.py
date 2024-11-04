# Importation du Blueprint depuis Flask
from flask import Blueprint, render_template, request, redirect

# Création d'un objet Blueprint nommé 'main_bp' avec un préfixe d'URL '/'
main_bp = Blueprint('main', __name__, url_prefix='/')

# Définition d'une route pour l'URL '/' avec la méthode GET
@main_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Définition d'une route pour l'URL '/submit' avec la méthode POST
@main_bp.route('/submit', methods=['POST'])
def submit():
    # Récupération des données du formulaire
    name = request.form['name']
    return f'Vous avez soumis le formulaire avec le nom: {name}'