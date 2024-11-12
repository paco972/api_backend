from flask import Flask, jsonify, request
from db import Database

app = Flask(__name__)

db = Database("192.168.1.xxx", "extern_user", "Bt5@c13l972", "ciel2025")

@app.route("/login")
def login():
    data = db.log(request)
    if data != 401:
        user = {
            "username": data[1],
            "password": data[2]
        }
        return jsonify(user), 200
    else: 
        return jsonify("Bad credentials"), 404
    
@app.route('/v3/etudiants/', methods=['GET'])
def getEtudiants():
    if db.authorized(request) == 500:
        return jsonify({'message': 'Echec de connexion à la base de données'}), 500
    if db.authorized(request) == 401:
        return jsonify({'message': 'Accès non autorisé'}), 401
    
    etudiants = []
    data = db.readAll()
    if data == 400:
        return jsonify("Requête invalide"), 400
    for row in data:
        etudiant = {
            "idetudiant": row[0],
            "nom": row[1],
            "prenom": row[2],
            "email": row[3],
            "telephone": row[4]
            }
        etudiants.append(etudiant)
    return jsonify(etudiants), 200

@app.route('/v3/etudiants/<int:id>', methods=['GET'])
def getEtudiant(id):
    code = db.authorized(request)
    if code == 500:
        return jsonify({'message': 'Echec de connexion à la base de données'}), 500
    if code == 401:
        return jsonify({'message': 'Accès non autorisé'}), 401
    
    data = db.readOne(id)
    if data == 400:
        return jsonify("Requête invalide"), 400
    if data != 404:
        etudiant = {
            "idetudiant": data[0],
            "nom": data[1],
            "prenom": data[2],
            "email": data[3],
            "telephone": data[4]
        }
        return jsonify(etudiant), 200
    else: 
        return jsonify("id invalide"), 404

if __name__ == '__main__':
    #app.run(host='0.0.0.0', port = 3000, debug=True)
    app.run(host='0.0.0.0', port = 3000, debug=True, ssl_context=('cert.pem', 'privkey.pem'))
