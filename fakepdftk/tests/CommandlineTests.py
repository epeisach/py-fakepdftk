##
#
# File:    CommandlineTests.py
# Author:  E.Peisach
# Date:    20-Sep-2018
# Version: 0.001
#
# Updates:
#
##
"""
Test cases for watermark rendering from command line

"""
__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "ezra.peisach@rcsb.org"
__license__ = "Apache 2.0"

import os
import sys
import unittest

HERE = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(os.path.dirname(HERE))

try:
    from fakepdftk import __version__
except Exception as e:  # noqa: F841 pylint: disable=bare-exxcept
    sys.path.insert(0, TOPDIR)
    from fakepdftk import __version__  # noqa: F401

from fakepdftk.command_line import main


class WatermarkTests(unittest.TestCase):
    def setUp(self):
        #print("Setup")
        self.__pathInputFile = os.path.join(HERE, 'data', '1o08_full_validation.pdf')
        self.__pathWatermarkFile = os.path.join(HERE, 'data', 'confidential.pdf')
        self.__pathOutputFile = os.path.join(HERE, 'output.pdf')
        if os.path.exists(self.__pathOutputFile):
            os.unlink(self.__pathOutputFile)

    def tearDown(self):
        #print("Teardown")
        pass

    def testSimpleCommand(self):
        """ Tests command line file output creation
        """
        status = main([self.__pathInputFile,
                       'background', self.__pathWatermarkFile,
                       'output', self.__pathOutputFile])
        self.assertTrue(status, "Failure from watermark generation")
        self.assertTrue(os.path.exists(self.__pathOutputFile),
                        "Failure to create output file")

    def testFailedWatermarkFileCreation(self):
        """ Tests missing files from commandline
        """
        with self.assertRaises(Exception) as context:
            main(["/tmp/a21234.pdf",
                  'background', self.__pathWatermarkFile,
                  'output', self.__pathOutputFile])

            self.assertTrue("Could not read PDF" in context.exception)
        self.assertFalse(os.path.exists(self.__pathOutputFile),
                         "Failure to NOT create output file")
