#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command

import sys

tests_require = []

# add unittest2 to tests_require for python < 2.7
if sys.version_info < (2, 7):
    tests_require.append("unittest2")


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """
        Finds all the tests modules in tests/, and runs them.
        """
        from tornado_mysqlreplication import tests
        import unittest

        unittest.main(tests, argv=sys.argv[:1])


version = "0.14"

setup(
    name="tornado-mysqlreplication",
    version=version,
    url="https://github.com/Jen94/tornado-mysql-replication",
    author="Evgeny Shakhov",
    author_email="jen9471@yandex.ru",
    description=("Pure Python Implementation of MySQL replication protocol "
                 "build on top of Tornado-MySQL."),
    license="Apache 2",
    packages=["tornado_mysqlreplication",
              "tornado_mysqlreplication.constants",
              "tornado_mysqlreplication.tests"],
    cmdclass={"test": TestCommand},
    extras_require={'test': tests_require},
    install_requires=['tornado', 'Tornado-MySQL'],
)
