## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

## Déploiement

Le déploiement de l'application s'effectue via un pipeline CircleCI. 
Le fichier de configuration `.circleci/config.yml` défini le *workflow* de déploiement.

Tout *push* sur le dépôt distant GitHub lié déclenche le *workflow* CircleCI, quelque soit la branche. L'application passe par une phase de construction (image Docker), puis de *linting* et de test.

En revanche, les *pushs* sur la branche *master* permettent, eux, de déclencher la suite  du *workflow*.

Lors d'un push sur la branche *master* :
- construction d'une image Docker générique, *linting* et test de l'application
- une image Docker définie est construite (*Dockerfile* à la racine du projet)
- elle est publiée sur DockerHub
- elle est déployée sur Heroku pour rendre l'application disponible

Chaque *job* doit être validé pour passer au suivant.

### Étapes
- Mettre en place le projet sur CircleCI en liant le dépôt GitHub
- Sélectionner le fichier de configuration `.circleci/config.yml`
- Définir les variables d'environnement dans les réglages du projet sur CircleCI :
  - DOCKERHUB_USERNAME
  - DOCKER_PASSWORD
  - HEROKU_API_KEY
  - HEROKU_LOGIN
  - HEROKU_APP_NAME
- Créer l'application sur Heroku (même nom que dans HEROKU_APP_NAME)
- *Push* vers une branche autre que *master* pour uniquement déclencher la phase *build-and-test*
- *Push* vers la branche *master* pour effectuer le déploiement complet sur Heroku

## Surveillance
La surveillance de l'application est effectué par Sentry.

Pour reconfigurer vers un autre projet Sentry, il faudra modifier l'url de la variable `dsn` à la fin du fichier `oc_lettings_site/settings.py` dans ```sentry_sdk.init()```
