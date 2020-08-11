#!/usr/bin/python3
""" console tests """

import unittest
import datetime
from uuid import UUID
import json
import os
import pep8
from console import HBNBCommand


class test_console(unittest.TestCase):
    """ test for console.py"""

    def test_pep8_console(self):
        """Pep8 console.py"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(["console.py"])
        self.assertEqual(p.total_errors, 0)
    
    def test_class_existence(self):
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("hello command")
            self.assertEqual("** class doesn't exist **\n", f.getvalue())
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
            self.assertEqual("** class name missing **\n", f.getvalue())
