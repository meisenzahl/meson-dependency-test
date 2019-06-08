#!/usr/bin/env python3
import os
from subprocess import Popen, PIPE, STDOUT
import unittest

def runCmd(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = p.communicate()
    
    if p.returncode != 0:
        print(output)
        exit(p.returncode)

def updateMeson():
    runCmd("cd meson && git checkout nested-subprojects && git pull")

def checkoutMeson():
    runCmd("git clone -b nested-subprojects git@github.com:semasquare/meson.git")

class NestedSubprojects(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.isdir("meson"):
            print("Updating meson with support for nested subprojects")
            updateMeson()
        else:
            print("Checking out meson with support for nested subprojects")
            checkoutMeson()

    def testCase01(self):
        self.assertTrue(False)

    def testCase02(self):
        self.assertTrue(False)

    def testCase03(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
