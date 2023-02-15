#!/usr/bin/python3
""" Test for console.py """

import unittest
import io
import sys
from unittest.mock import patch
from console import HBNBCommand
import cmd


class TestHBNBCcommand(unittest.TestCase):
    "Complete test suite for HBNBCommand cmd"""

    def setUp(self):
        """ set up the test """
        self.cmd = HBNBCommand()
        self.stdout = io.StringIO()
        sys.stdout = self.stdout

    def tearDown(self):
        """ Clean up after test"""
        sys.stdout = sys.__stdout__

    def test_is_instance_of_cmd(self):
        """Test that HBNBCommand is an instane
           of cmd.Cmd
        """
        self.assertIsInstance(self.cmd, cmd.Cmd)

    def test_do_quit_and_do_EOF(self):
        """
            Test if HBNBCommand implements quit
            EOF
        """
        self.assertTrue(self.cmd.onecmd("quit"))
        self.assertTrue(self.cmd.onecmd("EOF"))


if __name__ == "__main__":
    unittest.main()
