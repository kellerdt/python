#!c:/Python33 python

import sys # Adds custom module location for imports
sys.path.append('c:/code/python')

import imp
import os.path
import properties
import webfileutils

# Initialize global variables for managing files
props = properties.Cache()
props.load('c:/code/python','yume')
#fileutils = imp.load_source('c:/code/python/webfileutils.pyw')

def createComment(text):
	"""Creates a new comment in the community"""
	
	pass

def deleteComment():
	"""Allow access to remove an unwanted comment"""
	pass
