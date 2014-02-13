#include "helper.h"
#include <QtSql/QtSql>

Helper::Helper(QObject *parent) :
    QObject(parent)
{
}

bool Helper::dbConnect()
{
    QSqlDatabase db = QSqlDatabase::addDatabase("QPSQL");
    db.setHostName("localhost");
    db.setDatabaseName("pythonthusiast");
    db.setUserName("postgres");
    db.setPassword("adminadmin");
    return db.open();
}

QString Helper::computeHash(QString original)
{

    return QString(QCryptographicHash::hash(original.toUtf8(),QCryptographicHash::Md5).toHex());
}
