#include "mainwindow.h"
#include "logindialog.h"
#include <QApplication>
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    LoginDialog login;
    bool isAuth = false;
    int result;
    do
    {
        result = login.exec();
        isAuth = result == LoginDialog::Success || result == LoginDialog::Rejected;
    } while(!isAuth);

    if(result == LoginDialog::Success)
    {
        MainWindow w;
        w.show();
        return a.exec();
    }


    a.quit();
    return -1;
}
