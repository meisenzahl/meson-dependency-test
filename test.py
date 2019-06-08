#!/usr/bin/env python3
import os
import shutil
from subprocess import Popen, PIPE, STDOUT
import unittest

def runCmd(cmd, exitOnError=False, verbose=False):
    p = Popen(cmd, shell=True, stdout=PIPE, stderr=STDOUT)
    output = p.communicate()[0]

    if p.returncode == 0 and verbose:
        print(output.decode("utf-8"))
    elif p.returncode != 0:
        print(output.decode("utf-8"))

        if exitOnError:
            exit(p.returncode)

    return p.returncode

def updateMeson():
    runCmd(
        "cd meson && git checkout nested-subprojects && git pull",
        exitOnError=True
    )

def checkoutMeson():
    runCmd(
        "git clone -b nested-subprojects git@github.com:semasquare/meson.git",
        exitOnError=True
    )

def runMeson(dir):
    meson = "python3 {}".format(os.path.abspath("meson/__main__.py"))

    return runCmd("cd {} && {} build".format(dir, meson))

def cleanProjectDirectory(dir):
    build = os.path.join(dir, "build")

    if os.path.exists(build):
        shutil.rmtree(build)

    subprojects = os.path.join(dir, "subprojects")

    if os.path.exists(subprojects):
        for f in os.listdir(subprojects):
            if not f.endswith(".wrap"):
                shutil.rmtree(os.path.join(subprojects, f))

class NestedSubprojects(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if os.path.isdir("meson"):
            print("Updating meson with support for nested subprojects")
            updateMeson()
        else:
            print("Checking out meson with support for nested subprojects")
            checkoutMeson()

    def testCase01(self, dir="test/nested-subprojects/01"):
        cleanProjectDirectory(dir)

        self.assertEqual(runMeson(dir), 0)

    def testCase02(self, dir="test/nested-subprojects/02"):
        cleanProjectDirectory(dir)

        self.assertEqual(runMeson(dir), 0)

    def testCase03(self, dir="test/nested-subprojects/03"):
        cleanProjectDirectory(dir)

        self.assertEqual(runMeson(dir), 0)

if __name__ == "__main__":
    unittest.main()
