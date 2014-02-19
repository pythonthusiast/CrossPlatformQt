#include <QtGui/QApplication>
#include "mainwindow.h"
#include "logindialog.h"
#include <QDebug>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    LoginDialog login;
    if(login.exec() == QDialog::Accepted)
    {
        MainWindow w;
        w.show();
        return a.exec();
    }
    
    a.quit();
    return 0;
}
