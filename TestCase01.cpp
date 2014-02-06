#include <QtTest/QtTest>
class TestCase01: public QObject
{
    Q_OBJECT
private slots:
    void testAuth();
};

void TestCase01::testAuth()
{
    QCOMPARE("actual", "expected");
}

QTEST_MAIN(TestCase01)
#include "TestCase01.moc"
