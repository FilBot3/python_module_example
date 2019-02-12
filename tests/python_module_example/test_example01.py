#!python
# -*- coding: utf-8 -*-

import unittest

import python_module_example.example01

class TestExample01(unittest.TestCase):
  def test_say(self):
    self.assertEqual(python_module_example.example01.say(), 'Hello World!')

if __name__ == '__main__':
  unittest.main()
