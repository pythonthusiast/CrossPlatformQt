#ifndef AUTH_H
#define AUTH_H

#include <QObject>

class Auth : public QObject
{
    Q_OBJECT
public:
    explicit Auth(QObject *parent = 0);
    
signals:
    
public slots:
    bool doLogin();
    
};

#endif // AUTH_H
