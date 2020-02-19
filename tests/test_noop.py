from unittest import TestCase


class NoOpTestCase(TestCase):
    def test_no_op(self):
        self.assertTrue(True)
