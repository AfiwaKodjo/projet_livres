# API GESTION DES LIVRES

## Motivations
Cette API permet de gérer les livres d'une bibliothèque.
## Début

###  Installation des dépendances

#### Python 3.9.6
#### pip 21.1.3 from c:\users\kodjo\appdata\local\programs\python\python39\lib\site-packages\pip (python 3.9)

Si vous n'avez pas python installé, merci de suivre cet URL pour l'installer [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Environnement virtuel

Vous devez installer le package dotenv en utilisant la commande pip install python-dotenv 

#### Dépendances de PIP

Exécuter la commande ci dessous pour installer les dépendances
'''bash
configuration requise pour pip install -r.txt
ou
configuration requise pour pip3 install -r.txt
```

Cela installera tous les paquets requis que nous avons sélectionnés dans le fichier 'requirements.txt'.

##### Clés de dépendance

- [Flask] (http://flask.pocoo.org/) est un petit framework web Python qui fournit des outils et des fonctionalités utiles qui modifient la création des applications web en python.
- [SQLAlchemy] (https://www.sqlalchemy.org/) est la boîte à outils Python SQL et ORM que nous utiliserons pour gérer la base de données. Vous travaillerez principalement dans app.py.
- [Flacon-CORS] (https://flask-cors.readthedocs.io/en/latest/#) est l’extension que nous utiliserons pour gérer les demandes d’origine croisée de notre serveur frontal. 


## Exécution du serveur

À partir du répertoire 'projet_livres', assurez-vous d’abord que vous travaillez à l’aide de l’environnement virtuel que vous avez créé.

Pour exécuter le serveur sous Linux ou Mac, exécutez :

'''bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
Pour exécuter le serveur sous Windows, exécutez :

'''bash
set FLASK_APP=app.py
set FLASK_ENV=development
flask run
```

Définir la variable 'FLASK_ENV' sur 'development' détectera les modifications de fichiers et redémarrera automatiquement le serveur.

En définissant la variable 'FLASK_APP' sur 'app.py', flask doit utiliser le répertoire 'app.py' et le fichier '__init__.py' pour trouver l’application. 

## RÉFÉRENCE DE L’API

Démarrage

URL de base : à l’heure actuelle, cette application ne peut être exécutée que localement et n’est pas hébergée en tant qu’URL de base. L’application backend est hébergée par défaut, http://localhost:5000 ; qui est défini comme proxy dans la configuration frontale.

## Gestion des erreurs
Les erreurs sont renvoyées en tant qu’objets JSON au format suivant :
{   "success":False
    "error": 400
    "message":"Bad request"
}

L’API trois quatre types d’erreur en cas d’échec des demandes :
. 400: Bad request
. 500: Internal server error
. 404: Not found

## Points finaux
. ## GET/livres

GENERAL: cet endpoint permet de récupérer la liste de tous les livres,la valeur du succès et le total des livres.

EXEMPLE:http://localhost:5000/livres

{
  "livre": [
    {
      "auteur": "takaye", 
      "categorie_id": null, 
      "date_publication": "Thu, 25 Nov 2021 00:00:00 GMT", 
      "editeur": "scanfr", 
      "id": 4, 
      "isbn": "europe", 
      "titre": "solo leveling"
    }, 
    {
      "auteur": "lovestory", 
      "categorie_id": 1, 
      "date_publication": "Fri, 14 Feb 2020 00:00:00 GMT", 
      "editeur": "loveyou", 
      "id": 5, 
      "isbn": "europe", 
      "titre": "amour ou amitie"
    }
  ], 
  "success": true, 
  "total_livres": 2
}

 ## GET/livres(id)

GENERAL: cet endpoint permet de récupérer un livre en particulier.
        Les résultats de cette requete se présentent comme suit: 
EXEMPLE :GET http://localhost:5000/livres/5

{
  "id": 5, 
  "livre": {
    "auteur": "lovestory", 
    "categorie_id": 1, 
    "date_publication": "Fri, 14 Feb 2020 00:00:00 GMT", 
    "editeur": "loveyou", 
    "id": 5, 
    "isbn": "europe", 
    "titre": "amour ou amitie"
  }, 
  "success": true
}

. ## SUPPRIMER/livres (liv_id)

GENERAL: Cet endpoint permet de supprimer un etudiant
        Les résultats de cette requete se présentent comme suit:  
EXEMPLE :DELETE http://localhost:5000/livres/4

{ "success":True,
"deleted_id": 4,
 "total_livres": 1
 }
 
 . ##PATCH/livres(id)
 GÉNÉRALITÉS:
 Ce point de terminaison est utilisé pour mettre à jour un livre de la bibliothèque.
 Nous retournons un lvre que nous mettons à jour
 
  EXEMPLE..... Avec patch
  PATCH http://localhost:5000/livres/5
  
  {
    "auteur": "aimer", 
    "categorie_id": 1, 
    "date_publication": "Thur, 13 Feb 2020 00:00:00 GMT", 
    "editeur": "loveyoubae", 
    "id": 5, 
    "isbn": "asie", 
    "titre": "amour"
  }
  
  . ## GET/categories
  
  GENERAL: cet endpoint permet de récupérer la liste des catégories
  
  EXEMPLE: http://localhost:5000/categories
  
  {
  "categorie": [
    {
      "id": 2, 
      "libelle_categorie": "aventure"
    }, 
    {
      "id": 4, 
      "libelle_categorie": "fiction"
    }, 
    {
      "id": 1, 
      "libelle_categorie": "contes"
    }
  ], 
  "success": true, 
  "total_categorie": 3
}

## GET/categories(cate_id)

GENERAL: cet endpoint permet de récupérer une catégorie en particulier.
        Les résultats de cette requete se présentent comme suit: 
EXEMPLE :GET http://localhost:5000/categories/2

{
  "categorie": {
    "id": 2, 
    "libelle_categorie": "aventure"
  }, 
  "id": 2, 
  "success": true
}

. ## SUPPRIMER/categories (cat_id)
GENERAL: Cet endpoint permet de supprimer une catégorie
        Les resulats de cette requete se présentent comme suit:
         EXEMPLE : DELETE http://localhost:5000/categories/2
         
         {
                "success": True,
                "deleted_id": 2,
                "total_categories":2
                }
                
        . ##PATCH/livres(id)
        GÉNÉRALITÉS:
 Ce point de terminaison est utilisé pour mettre à jour le libellé catégorie du livre.
 Nous retournons un libellé catégorie que nous mettons à jour.
 
 EXEMPLE..... Pour patch
 PATCH http://localhost:5000/categories/4
 {
    "id": 4, 
    "libelle_categorie": "contes"
  }
  
  . ## GET/categories/categ(cate_id)
  
  GENERAL: cet endpoint permet de lister une catégorie
  
  EXEMPLE:GET http://localhost:5000/categories/categ/2
  
  {
  "Liste_categorie": {
    "id": 2, 
    "libelle_categorie": "aventure"
  }, 
  "success": true
}

. ## GET /categories/<int:id>/livres
  
  GENERAL: cet endpoint permet de lister les livres d'une catégorie
  
  EXEMPLE:GET http://localhost:5000/categories/1/livres
  
  {
  "classe": {
    "id": 1, 
    "libelle_categorie": "contes"
  }, 
  "livres": [
    {
      "auteur": "lovestory", 
      "categorie_id": 1, 
      "date_publication": "Fri, 14 Feb 2020 00:00:00 GMT", 
      "editeur": "loveyou", 
      "id": 5, 
      "isbn": "europe", 
      "titre": "amour ou amitie"
    }
  ], 
  "success": true, 
  "total_livre": 1
}


