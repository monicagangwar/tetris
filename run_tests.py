#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lib.test_runner import ModuleTestRunner
rom tests.test_sanity import TestSanity

suite = ModuleTestRunner()

suite.addTestList("Sanity", [TestSanity("test_fail"),
	TestSanity("test_pass"),
	])

if __name__ == '__main__':
	suite.run()

