#-------------------------------------------------
#
# Project created by QtCreator 2014-02-05T05:32:29
#
#-------------------------------------------------

QT       += testlib

QT       -= gui

TARGET = tst_testcase01test
CONFIG   += console
CONFIG   -= app_bundle

TEMPLATE = app


SOURCES += tst_testcase01test.cpp \
    auth.cpp
DEFINES += SRCDIR=\\\"$$PWD/\\\"

HEADERS += \
    auth.h
