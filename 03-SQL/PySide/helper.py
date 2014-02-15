from PySide.QtCore import *
from PySide.QtSql import *

def dbConnect():
    db = QSqlDatabase.addDatabase("QSQLITE")
    filename = "pythonthusiast.db"
    database =  QFile(filename)
    if not database.exists():
        qDebug("Database not found. Creating and opening")
        db.setDatabaseName(filename)
        db.open()
        query = QSqlQuery()
        query.exec_("create table qtapp_users "
                    "(id integer primary key autoincrement, "
                    "username varchar(30), "
                    "password varchar(255))")
        query.prepare("insert into qtapp_users(username, password) values(:username, :password)")
        query.bindValue(":username", "eko")
        query.bindValue(":password", computeHash("password"))
        query.exec_()
    else:
        qDebug("Database found. Opening")
        db.setDatabaseName(filename)
        db.open()
    return db.isOpen()

def computeHash(original):
    return QCryptographicHash.hash(original, QCryptographicHash.Md5).toHex()