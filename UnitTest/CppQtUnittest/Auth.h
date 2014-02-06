#ifndef AUTH_H
#define AUTH_H

#include <QObject>

class Auth: public QObject
{
	Q_OBJECT
public:
	bool doLogin(QString name, QString pass);
};
#endif
