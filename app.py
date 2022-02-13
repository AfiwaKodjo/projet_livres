#from urllib import request
from urllib.parse import quote_plus
from flask import Flask, jsonify,abort,request
from flask_sqlalchemy import SQLAlchemy
import os
from requests import get
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


passw = os.getenv("password_db")
#app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {"pool_pre_ping": True}  
#engine = create_engine("postgresql://postgres:soulager@localhost/bibliotheque", pool_pre_ping=True)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:{}@localhost:5432/bibliotheque'.format(
    passw)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

CORS(app)

# CORS(app, resources={r"/api/*": {"origin": "*"}})   #Préciser le domaine autoriser à interroger une api

migrate = Migrate(app, db)

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods',
                         'GET,PUT,POST,DELETE,OPTIONS')
    return response


# Mappage
class Categorie(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    libelle_categorie = db.Column(db.String(30), nullable=False)
    liv = db.relationship('Livre', backref='Categorie', lazy=True)

    def __init__(self,libelle_categorie):
        self.libelle_categorie=libelle_categorie

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
      return{
            'id':self.id,
            'libelle_categorie': self.libelle_categorie
            }                  

class Livre(db.Model):
    __tablename__ = "livres"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(30), nullable=False)
    titre = db.Column(db.String(50), nullable=False)
    date_publication = db.Column(db.Date, nullable=False)
    auteur = db.Column(db.String(50), nullable=False)
    editeur = db.Column(db.String(50), nullable=False)
    categorie_id = db.Column(db.Integer, db.ForeignKey('categories.id'))


    def __init__(self, isbn, titre, date_publication, auteur, editeur, categorie_id) :
        self.isbn = isbn
        self.titre = titre
        self.date_publication = date_publication
        self.auteur = auteur
        self.editeur = editeur
        self.Categorie_id = categorie_id

            
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'id': self.id,
            'isbn': self.isbn,
            'titre': self.titre,
            'date_publication': self.date_publication,
            'auteur': self.auteur,
            'editeur': self.editeur,
            'categorie_id': self.categorie_id
            }


def paginate(request):
    items = [item.format() for item in request]
    return items

#Lister tous les livres
@app.route('/livres',methods=['GET'])
def all_livres():
    livres = Livre.query.all()
    livres = [p.format() for p in livres]
    return jsonify({
        'success': True,
        'livre': livres,
        'total_livres': len(livres)
    })

# chercher un livre en particulier
@app.route('/livres/<int:id>')
def one_livre(id):
    try:
        livre = Livre.query.get(id)
        if livre is None:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'id': id,
                'livre': livre.format()
            })
    except:
        abort(400)

# Supprimer un livre
@app.route('/livres/<int:liv_id>', methods=['DELETE'])
def del_livre(liv_id):
    try:
        livre = Livre.query.get(liv_id)
        if livre is None:
            abort(404)
        else:
            livre.delete()
            return jsonify({
                "success": True,
                "deleted_id": liv_id,
                "total_livres": len(Livre.query.all())
            })
    except:
        abort(400)
    finally:
        db.session.close()



#Modifier les informations d'un livre
@app.route('/livres/<int:id>', methods=['PATCH'])
def update_livre(id):
    body = request.get_json()
    livre = Livre.query.get(id)
    try: 
        if 'isbn' in body and 'titre' in body and 'date_publication' in body and 'auteur' in body and 'editeur' in body:
           livre.isbn= body['isbn']
           livre.titre= body['titre']
           livre.date_publication= body['date_publication']
           livre.auteur= body['auteur']
           livre.editeur= body['editeur']
        
        livre.update()
        return jsonify({
            'success':True,
            'modifie':livre.format()
        })
    except:
        abort(400)
    
###### CATEGORIES ######

#Lister toutes les catégories
@app.route('/categories')
def all_categories():
    categories = Categorie.query.all()
    categories = [p.format() for p in categories]
    return jsonify({
        'success': True,
        'categorie': categories,
        'total_categorie': len(categories)
    })

# chercher une catégorie en particulier
@app.route('/categories/<int:cate_id>')
def one_categorie(cate_id):
        try:
            categorie = Categorie.query.get(cate_id)
            if categorie is None:
                abort(404)
            else:
                return jsonify({
                    'success': True,
                    'id': cate_id,
                    'categorie': categorie.format()
                })
        except:
            abort(400)


 #Supprimer une catégorie
@app.route('/categories/<int:cat_id>', methods=['DELETE'])
def del_categorie(cat_id):
    try:
        categorie = Categorie.query.get(cat_id)
        if categorie is None:
            abort(404)
        else:
            categorie.delete()
            return jsonify({
                "success": True,
                "deleted_id": cat_id,
                "total_categories": len(Categorie.query.all())
                })
    except:
        abort(400)
    finally:
        db.session.close()


#Modifier le libellé d'une catégorie
@app.route('/categories/<int:id>', methods=['PATCH'])
def update_categorie(id):
        body = request.get_json()
        categorie = Categorie.query.get(id)
        try:
            if 'libelle_categorie' in body:
                categorie.libelle_categorie = body['libelle_categorie']
            categorie.update()
            return categorie.format()
        except:
            abort(400)



#Lister une catégorie
@app.route('/categories/categ/<int:cate_id>')
def get_categorie(cate_id):
    categorie=Categorie.query.get(cate_id)
    if categorie is None:
        abort(404)
    else:
        return jsonify({
        'success':True,
        'Liste_categorie':categorie.format()

         })


#Lister la liste des livres d'une catégorie
@app.route('/categories/<int:id>/livres')
def get_categ(id):
    try:
        categorie=Categorie.query.get(id)
        livres=Livre.query.filter_by(categorie_id=id).all()
        livres=paginate(livres)
        return jsonify({
            'success':True,
            'total_livre':len(livres),
            'classe':categorie.format(),
            'livres':livres
        })
    except:
        abort(404)
    finally:
        db.session.close()

    
