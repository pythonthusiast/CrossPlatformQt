#include <QtTest/QtTest>
#include <QtSql/QtSql>
#include "auth.h"
#include "helper.h"

class TestCase01: public QObject
{
    Q_OBJECT
private:
    Auth auth;     
private slots:
    void initTestCase();
    void testAuth();
};

void TestCase01::initTestCase()
{
    QCOMPARE(Helper::dbConnect(), true);
}

void TestCase01::testAuth()
{
    QCOMPARE(auth.doLogin("eko", "oke"), true);
}

QTEST_MAIN(TestCase01)
#include "TestCase01.moc"
