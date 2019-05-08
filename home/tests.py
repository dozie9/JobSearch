#!/home/acer/anaconda3/bin/python python

from django.test import TestCase
import ast, sys

import JobSearch
import subprocess, os

# Create your tests here.
print(os.getcwd())
# rr = subprocess.check_output([sys.executable, './JobSearch.py', 'computer science intern'])
# print(rr.decode('utf-8'))

process = subprocess.Popen(['./JobSearch.py', 'computer science intern'], stdout=subprocess.PIPE)
stdout = process.communicate()
print(stdout[0].decode('utf-8'))