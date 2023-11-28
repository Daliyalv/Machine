from translator import translator
import unittest
import filecmp


class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print("Test of translator beginning:")

    def tearDown(self) -> None:
        print("Test of translator finished.")

    def test_hello(self):
        print("Testing hello")
        translator.translate("./asm/hello.asm", "./tmp/result.tmp")
        status = filecmp.cmp('./tmp/result.tmp', './target/hello')
        self.assertEqual(status, True)


    def test_cat(self):
        print("Testing cat")
        translator.translate("./asm/cat.asm", "./tmp/result.tmp")
        status = filecmp.cmp('./tmp/result.tmp', './target/cat')
        self.assertEqual(status, True)


    def test_prob5(self):
        print("Testing problem5")
        translator.translate("./asm/problem5.asm","result")
        status = filecmp.cmp('result', 'target/problem5')
        self.assertEqual(status, True)