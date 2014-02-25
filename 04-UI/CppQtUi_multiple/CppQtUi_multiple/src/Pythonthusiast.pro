#-------------------------------------------------
#
# Project created by QtCreator 2014-02-21T19:09:32
#
#-------------------------------------------------

QT       += core gui sql

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Pythonthusiast
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    logindialog.cpp \
    auth.cpp \
    helper.cpp

HEADERS  += mainwindow.h \
    logindialog.h \
    auth.h \
    helper.h

FORMS    += mainwindow.ui \
    logindialog.ui

RESOURCES += \
    app.qrc

OTHER_FILES += \
    ../../../../../Pictures/pythonthusiast/sherlock.jpg \
    sherlock.jpg \
    sherlock.png
