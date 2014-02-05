#include <QtTest/QtTest>
#include "auth.h"
class TestCase01: public QObject
{
    Q_OBJECT
private:
    Auth auth;
private slots:
    void testAuthX();
};

void TestCase01::testAuthX()
{
    QCOMPARE(false, auth.doLogin("eko", "oke"));
    QCOMPARE("eko", "eko");
}

QTEST_MAIN(TestCase01)
#include "TestCase01.moc"
