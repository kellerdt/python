#!c:/Python33 python

import os
import shutil

basedir = os.getcwd()

def setBaseDir(dir):
	"""Sets the base directory for file manipulations.  Default is CWD"""
	global basedir
	basedir = dir
	if not os.path.exists(basedir):
		os.mkdir(basedir)

def printFileStats(file):
	"""Outputs statistics about a file for debugging"""
	print ("Filename: ", file.name)
	print ("Closed status: ", file.closed)
	print ("Opening mode: ", file.mode)
	print ("Softspace flag: ", file.softspace)

def remove(dir, file):
	"""Removes a file from the directory"""
	path = os.path.join(basedir, dir)
	if os.path.exists(path):
		file = os.path.join(path, file)
		if os.path.exists(file):
			os.remove(file)
			return True
	return False

def move(src, dest, file):
	"""Moves a file from one directory to another"""
	src = os.path.join(basedir, src, file)
	dest = os.path.join(basedir, dest)
	if not os.path.exists(dest):
		os.mkdir(dest)
	dest = os.path.join(dest, file)
	if os.path.exists(src) and not os.path.exists(dest):
		shutil.copy(src, dest)
		if os.path.exists(dest):
			os.remove(src)
			return True
	return False

def create(dir, file, contents):
	"""Creates a file in the specified directory"""
	path = os.path.join(basedir, dir)
	if not os.path.exists(path):
		os.mkdir(path)
	file = open(os.path.join(path, file), 'w')
	file.write(contents)
	file.close()
	return file
