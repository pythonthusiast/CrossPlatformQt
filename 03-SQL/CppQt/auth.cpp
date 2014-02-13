#include "auth.h"
#include <QtSql>
bool Auth::doLogin(QString name, QString pass)
{
    QSqlQuery query;
    query.prepare("select id from qtapp_users where username = :username and password = md5(:password)");
    query.bindValue(":username", name);
    query.bindValue(":password", pass);
    query.exec();
    if(query.next()){
        return true;
    }
    return false;
}
