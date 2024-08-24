import psycopg2

class Conexion:

    """Metodo constructor
    """
    def _init_(self):
        self.con = psycopg2.connect("dbname=veterinaria-db user=postgres host=localhost password=admin")

    """getConexion

        retorno la instancia de la base de datos
    """
    def getConexion(self):
        return self.con
