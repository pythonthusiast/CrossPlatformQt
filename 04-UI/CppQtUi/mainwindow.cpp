#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <QDesktopWidget>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    setGeometry(
        QStyle::alignedRect(
            Qt::LeftToRight,
            Qt::AlignCenter,
            size(),
            qApp->desktop()->availableGeometry()
        ));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionE_xit_triggered()
{
    QMessageBox msgBox(this);
    msgBox.setWindowTitle(tr("Pythonthusiast"));
    msgBox.setText(tr("Are you sure you want to quit?"));
    msgBox.setStandardButtons(QMessageBox::No|QMessageBox::Yes);
    msgBox.setDefaultButton(QMessageBox::Yes);

    if(msgBox.exec()==QMessageBox::Yes)
    {
        qApp->quit();
    }

}

void MainWindow::on_action_About_triggered()
{
    QMessageBox msgBox(this);
    msgBox.setWindowTitle(tr("Pythonthusiast"));
    msgBox.setText(tr("Programmer : Eko SW\nGod speak in Python.. and then C++.. :D"));
    msgBox.setStandardButtons(QMessageBox::Ok);
    msgBox.exec();

}
