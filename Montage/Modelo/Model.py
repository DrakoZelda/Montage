from PyQt4 import QtSql

class Sistema(QtSql):
    def __init__(self):
        self.user = ""
        self.passwd = ""

    def initializeModel(self, model):
        model.setTable('empleados')
        model.select()

    def agregarEmpleado(self, user, passwd):
        query = QtSql.QSqlQuery()
        #revisar sintaxis insert
        query.exec_("insert into empleados values()")

    def agregarUsuario(self, user, passwd):
        query = QtSql.QSqlQuery()
        query.exec_("insert into usuarios values()")

    def HoraInicio(self, user, passwd):
        query = QtSq