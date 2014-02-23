#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_action_About_triggered()
{
    QMessageBox msgBox(this);
    msgBox.setIconPixmap(QPixmap(":/images/sherlock.png"));
    msgBox.setWindowTitle(tr("Pythonthusiast"));
    msgBox.setText(tr("Well Watson, isn't it obvious to you that Qt rocks?"));
    msgBox.setStandardButtons(QMessageBox::Ok);
    msgBox.exec();
}

void MainWindow::on_actionE_xit_triggered()
{
    QMessageBox msgBox(this);
    msgBox.setIcon(QMessageBox::Question);
    msgBox.setWindowTitle(tr("Pythonthusiast"));
    msgBox.setText(tr("Are you sure you want to quit?"));
    msgBox.setStandardButtons(QMessageBox::No|QMessageBox::Yes);
    msgBox.setDefaultButton(QMessageBox::Yes);

    if(msgBox.exec()==QMessageBox::Yes)
    {
        qApp->quit();
    }
}
