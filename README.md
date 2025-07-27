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

### Sentry

1. Créer un compte sur https://sentry.io et un projet Django.
2. Récupèrer le DSN du projet.
3. L'ajouter dans un fichier `.env` (ex: SENTRY_DSN=https://<your-key>@o123456.ingest.sentry.io/12345678)
4. Lors du déploiement, ajouter `SENTRY_DSN` dans les variables d’environnement du serveur.

### Déploiement

#### Vue d’ensemble

Ce projet utilise une **pipeline CI/CD automatisée** avec GitHub Actions, Docker et Render :

* À chaque **commit sur une branche autre que `master`**, les **tests** et le **linting** sont lancés.
* À chaque **commit sur la branche `master`** :

  1. Les tests et le linting sont exécutés.
  2. Si tout est OK, une **image Docker** est construite et **poussée sur Docker Hub**.
  3. Une fois l’image poussée, **Render** il faut déployer manuellement la nouvelle version du site.

#### Configuration requise

Pour que le déploiement fonctionne correctement, s'assurer que :

* Un **compte Docker Hub** est configuré avec un repository public ou privé pour l’image.
* Un **compte GitHub** héberge le projet avec le fichier de pipeline `.github/workflows/ci-cd.yml`.
* Un **compte Render** est configuré avec un service Docker connecté au repo GitHub.
* Les **secrets GitHub** suivants sont bien ajoutés dans les paramètres du dépôt :

  * `DOCKER_USERNAME` → identifiant Docker Hub
  * `DOCKER_PASSWORD` → mot de passe ou token Docker Hub

#### 🔑 Variables d’environnement (Render)

Ajouter ces variables d’environnement dans la section "Environment" de Render :

| Nom             | Valeur                                         |
| --------------- | ---------------------------------------------- |
| `DEBUG`         | `False` (important en production)              |
| `SECRET_KEY`    | une clé secrète Django sécurisée               |
| `ALLOWED_HOSTS` | `your-app-url.render.com`                      |
| `SENTRY_DSN`    | `https://url@exemple.ingest.de.sentry.io/`     |

#### 🧪 Lancer localement l’application via Docker

1. Créer un fichier `.env` à la racine du projet :

  ```env
  DEBUG=False
  SECRET_KEY=your-secret-key
  ALLOWED_HOSTS=127.0.0.1,localhost
  ```

2. Construire l’image :

  ```bash
  docker build -t oc-lettings-site .
  ```

3. Lancer le conteneur :

  ```bash
  docker run -p 8000:8000 --env-file .env oc-lettings-site
  ```

#### Déployer une nouvelle version

1. **Pousser un commit sur `master`** :

   ```bash
   git checkout master
   git commit -m "Nouvelles modifications"
   git push origin master
   ```

2. GitHub Actions va :

   * Lancer tests + lint
   * Construire et pusher l’image Docker sur Docker Hub

3. Sur **Render**, déclencher manuellement le déploiement via l’interface (“Manual Deploy”) si le déploiement automatique est désactivé.
