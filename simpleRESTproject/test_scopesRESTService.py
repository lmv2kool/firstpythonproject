import unittest
from simpleRESTproject.restservermodule import ScopesRESTService

__author__ = 'vivekl'


class TestScopesRESTService(unittest.TestCase):
  def test_index(self):
    self.fail()

  def test_get_scope(self):
    test_object = ScopesRESTService()
    expected_output = ['PLMN-PLMN/RNC-148/WBTS-1/WCEL-1', 'PLMN-PLMN/RNC-148/WBTS-1/WCEL-2']
    actual_output = (test_object.get_scope('SCM_scope'))
    self.assertListEqual(expected_output, actual_output)

  def test_addscope(self):
    self.fail()

if __name__ == '__main__':

    unittest.main()