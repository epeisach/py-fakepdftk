##
#
# File:    WatermarkTests.py
# Author:  E.Peisach
# Date:    20-Sep-2018
# Version: 0.001
#
# Updates:
#
##
"""
Test cases for watermark rendering

"""
__docformat__ = "restructuredtext en"
__author__ = "Ezra Peisach"
__email__ = "ezra.peisach@rcsb.org"
__license__ = "Apache 2.0"

import os
import unittest

HERE = os.path.abspath(os.path.dirname(__file__))
TOPDIR = os.path.dirname(os.path.dirname(HERE))

from fakepdftk.WatermarkUtils import WatermarkUtils


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

    def testWatermarkFileCreation(self):
        """ Tests file output creation
        """
        wM = WatermarkUtils()
        status = wM.addWatermarkFile(self.__pathInputFile,
                                     self.__pathWatermarkFile,
                                     self.__pathOutputFile)
        self.assertTrue(status, "Failure from watermark generation")
        self.assertTrue(os.path.exists(self.__pathOutputFile),
                        "Failure to create output file")

    def testFailedWatermarkFileCreation(self):
        """ Tests missing files
        """
        wM = WatermarkUtils()

        with self.assertRaises(Exception) as context:
            wM.addWatermarkFile("/tmp/a1234vdvvj.pdf",
                                self.__pathWatermarkFile,
                                self.__pathOutputFile)
            self.assertTrue("Could not read PDF" in context.exception)
        self.assertFalse(os.path.exists(self.__pathOutputFile),
                         "Failure to create output file")
