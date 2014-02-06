#include <QtTest/QtTest>
#include "auth.h"

class TestCase01: public QObject
{
    Q_OBJECT
private:
    Auth auth;     
private slots:
    void testAuth();
};

void TestCase01::testAuth()
{
    QCOMPARE(auth.doLogin("eko", "oke"), true);
}

QTEST_MAIN(TestCase01)
#include "TestCase01.moc"
