import unittest

class TestSanity(unittest.TestCase):
	def test_fail(self):
		self.assertTrue(False)
	def test_pass(self):
		self.assertTrue(True)
