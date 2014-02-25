#include "mainwindow.h"
#include "logindialog.h"
#include <QApplication>
#include "helper.h"
int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    Helper::dbConnect();
    LoginDialog login;
    bool isAuth = false;
    int result;
    while(!isAuth){
        result = login.exec();
        isAuth = result == LoginDialog::Success || result == LoginDialog::Rejected;
    }

    if(result == LoginDialog::Success)
    {
        MainWindow w;
        w.show();
        return a.exec();
    }


    a.quit();
    return 0;
}
