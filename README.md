# Internal Tools API

## Technologies

- Langage: Python
- Framework: Django
- Base de données: PostgreSQL
- Port API: 8000

## Configuration

1. `docker-compose --profile postgres up -d`

2. `python -m venv env` sous Windows ou `python3 -m venv env` sous MacOS ou Linux.
3. Activez l'environnement avec `./env/Scripts/activate` sous Windows ou `source env/bin/activate` sous MacOS ou Linux.
4. Installez les dépendances du projet avec la commande `pip install -r requirements.txt`
5. Définir les variables d'environnement dans un fichier .env ainsi :

```
SECRET_KEY=*******
DEBUG=******
ALLOWED_HOSTS=******* ******
POSTGRES_USER=*******
POSTGRES_PASSWORD*******
```

6. Créer la base de données avec `createdb -U UserName internal_tools`
7. Appliquer les migrations `python manage.py migrate`
8. Alimenter la base de données des utilisateurs `python manage.py loaddata accounts/fixtures/authentication.json`
9. Alimenter la base de données des outils `manage.py loaddata toolsmanagement/fixtures/tools.json`
   En cas de problème d'encodage, ne pas hésiter à utiliser un éditeur pour ouvrir et sauvegarder les fichiers JSON avec l'encodage utf-8. Puis réalimenter (étape 8 et 9).

10. Démarrer le serveur avec la commande `python manage.py runserver`
11. API disponible sur http://localhost:8000
12. Documentation Swagger http://localhost:8000/swagger/

## Tests

Tests unitaires avec `python manage.py runserver`

## Architecture

- [Justification_choix_tech]
- [Structure_projet_expliquee]
