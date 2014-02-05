#include <QtCore/QString>
#include <QtTest/QtTest>
#include "auth.h"
class TestCase01Test : public QObject
{
    Q_OBJECT
private:
    Auth auth;
public:
    TestCase01Test();


private Q_SLOTS:
    void initTestCase();
    void cleanupTestCase();
    void testAuth2();
};

TestCase01Test::TestCase01Test()
{
}

void TestCase01Test::initTestCase()
{

}

void TestCase01Test::cleanupTestCase()
{
}

void TestCase01Test::testAuth2()
{
    QCOMPARE(false, auth.doLogin());
    QVERIFY2(true, "Failure");
}

QTEST_APPLESS_MAIN(TestCase01Test)

#include "tst_testcase01test.moc"
