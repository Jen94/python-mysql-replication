# -*- coding: utf-8 -*-

from tornado_mysqlreplication.tests.test_basic import *
from tornado_mysqlreplication.tests.test_data_type import *
from tornado_mysqlreplication.tests.test_data_objects import *

if __name__ == "__main__":
    if sys.version_info < (2, 7):
        import unittest2 as unittest
    else:
        import unittest
    unittest.main()
