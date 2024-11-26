import mysql.connector
import hashlib

class Database:

    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database 
        
    def connect(self):
        connector = mysql.connector.connect(
            host = self.host, 
            user = self.user, 
            password = self.password, 
            database = self.database)
        return connector
        
    def readAll(self):
        conn = self.connect()
        curs = conn.cursor()
        try:
            curs.execute(f"SELECT * FROM etudiant")
            data = curs.fetchall() 
            return data
        except:
            return 400
        finally:
            conn.close()

    def readOne(self, id):
        conn = self.connect()
        curs = conn.cursor()
        try:
            curs.execute(f"SELECT * FROM etudiant WHERE idEtudiant = {id}")
            data = curs.fetchone() 
            if data:
                return data
            else:
                return 404
        except:
            return 400
        finally:
            conn.close()
        
    def create(self):
        pass

    def update(self, id):
        pass
    
    def delete(self, id):
        pass

    def authorized(self, request):
        try:
            auth = request.authorization
            username = auth.username
            password = auth.password
        except:
            return 401
        try:
            conn = self.connect()
            curs = conn.cursor()
        except:
            return 500        
        try:
            curs.execute(f"SELECT password FROM user WHERE login = '{username}'")
            data = curs.fetchone() 
            if data and (data[0] == password):
                return 200
            else:
                return 401
        except:
            return(401)
        finally:
            conn.close()
    
    def log(self, request):
        try:
            auth = request.authorization
            username = auth.username
            password = hashlib.sha256(auth.password.encode('utf-8')).hexdigest()
        except:
            return 401
        try:
            conn = self.connect()
            curs = conn.cursor()
        except:
            return 500        
        try:
            curs.execute(f"SELECT * FROM user WHERE login = '{username}' AND password = '{password}'")
            data = curs.fetchone() 
            if data:
                return data
            else:
                return 401
        except:
            return(401)
        finally:
            conn.close()
