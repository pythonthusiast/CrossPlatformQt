#include "helper.h"
#include <QtSql/QtSql>

Helper::Helper(QObject *parent) :
    QObject(parent)
{
}

bool Helper::dbConnect()
{
    //If using Sqlite
    QSqlDatabase db = QSqlDatabase::addDatabase("QSQLITE");
    QString filename = "pythonthusiast.db";
    QFile database(filename);
    if(!database.exists())
    {
        qDebug() << "Database not found. Creating and opening";
        db.setDatabaseName(filename);
        db.open();
        QSqlQuery query;
        query.exec("create table qtapp_users "
                    "(id integer primary key autoincrement, "
                    "username varchar(30), "
                    "password varchar(255))");
        query.prepare("insert into qtapp_users(username, password) values(:username, :password)");
        query.bindValue(":username", "eko");
        query.bindValue(":password", Helper::computeHash("password"));
        query.exec();
    }
    else
    {
        qDebug() << "Database found. Opening";
        db.setDatabaseName(filename);
        db.open();
    }

    //If using PostgreSQL
    /*
    QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
    db.setHostName("localhost");
    db.setDatabaseName("pythonthusiast");
    db.setUserName("postgres");
    db.setPassword("adminadmin");
    db.open();
    */

    return db.isOpen();
}

QString Helper::computeHash(QString original)
{
    return QCryptographicHash::hash(original.toUtf8(),QCryptographicHash::Md5).toHex();
}
