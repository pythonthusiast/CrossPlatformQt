from PySide.QtSql import *
import helper

class Auth:
    def doLogin(self, username, password):
        query = QSqlQuery()
        query.prepare("select id from qtapp_users where username = :username and password = :password")
        query.bindValue(":username", username)
        query.bindValue(":password", helper.computeHash(password))
        query.exec_()
        if query.next():
            return True
        return False