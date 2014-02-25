#include <QtTest/QtTest>
#include <QtSql/QtSql>
#include "../src/auth.h"
#include "../src/helper.h"

class TestCase01: public QObject
{
    Q_OBJECT
private:
    Auth auth;     
private slots:
    void initTestCase();
    void testMd5();
    void testAuth();
};

void TestCase01::initTestCase()
{
    QCOMPARE(Helper::dbConnect(), true);
}

void TestCase01::testMd5()
{
    QCOMPARE(Helper::computeHash("password"), QString("5f4dcc3b5aa765d61d8327deb882cf99"));
}

void TestCase01::testAuth()
{
    QCOMPARE(auth.doLogin("eko", "password"), true);
}

QTEST_MAIN(TestCase01)
#include "TestCase01.moc"
