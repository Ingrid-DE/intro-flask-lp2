import psycopg2

class Conexion:

    """Metodo constructor
    """
    def __init__(self):
        self.con = psycopg2.connect(dbname="veterinaria-db", user="postgres", password="19082003", host="localhost", port=5432)
        #self.con = psycopg2.connect("dbname=veterinaria-db user=postgres host=127.0.0.1 port=5433 password=admin")
    """getConexion

        retorno la instancia de la base de datos

    """
   
    
    def getConexion(self):
        return self.con
