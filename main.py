#!/usr/bin/env python
# -*- coding: utf-8 -*-


import fnmatch
import os
import argparse

# header of file to get args
parser = argparse.ArgumentParser(description='Replace the string you want in all files of path')
parser.add_argument('path', metavar='path', type=str, help='Path where it will find the files')
parser.add_argument('string', metavar='string', type=str, help='the string to be replaced')
parser.add_argument('replace', metavar='replace', type=str, help='the string to replace (optional)', default='', nargs='?')
args = parser.parse_args()

matches = 0
for root, dirnames, filenames in os.walk(args.path):
    for filename in fnmatch.filter(filenames, '*' + args.string + '*'):
    	srcFile = os.path.join(root, filename)
    	destFile = os.path.join(root, filename.replace(args.string, args.replace))
    	os.rename(srcFile, destFile)
    	matches += 1

print("Renamed %d files" % matches)