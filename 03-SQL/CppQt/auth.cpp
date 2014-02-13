#include "auth.h"
#include <QtSql>
bool Auth::doLogin(QString name, QString pass)
{
    QSqlQuery query;
    query.exec("SELECT");
	return name == "eko";
}
