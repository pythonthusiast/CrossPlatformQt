#include "auth.h"
#include <QtSql>
#include "helper.h"

bool Auth::doLogin(QString name, QString pass)
{
    QSqlQuery query;
    query.prepare("select id from qtapp_users where username = :username and password = :password");
    query.bindValue(":username", name);
    query.bindValue(":password", Helper::computeHash(pass));
    query.exec();
    if(query.next()){
        return true;
    }
    return false;
}
