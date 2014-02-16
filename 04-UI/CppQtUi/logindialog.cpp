#include "logindialog.h"
#include "ui_logindialog.h"
#include <QDesktopWidget>

LoginDialog::LoginDialog(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::LoginDialog)
{
    ui->setupUi(this);
    setGeometry(
        QStyle::alignedRect(
            Qt::LeftToRight,
            Qt::AlignCenter,
            size(),
            qApp->desktop()->availableGeometry()
        ));
    ui->txtUsername->setFocus();
}

LoginDialog::~LoginDialog()
{
    delete ui;
}

void LoginDialog::on_buttonBox_accepted()
{
    if(ui->txtUsername->text()=="eko")
    {
        setResult(QDialog::Accepted);
    }else{
        setResult(QDialog::Rejected);
    }
}
