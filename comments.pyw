#!c:/Python33 python

import sys # Adds custom module location for imports
sys.path.append('c:/code/python')

import imp
import os
import os.path
import properties
import webfileutils

class File:
	def create(text):
		"""Creates a new comment in the community"""
		properties.Cache.load('c:/code/python','fileComments')
		baseDir = properties.Cache.get('baseDir')
		text = '<p>' + text + '</p>'
		webfileutils.setBaseDir(baseDir)
		curFiles = os.listdir(os.path.join(baseDir,'test'))
		
		max = -1
		min = 5000000
		for curFile in curFiles:
			fileValue = int(curFile[:-5])
			if fileValue < min:
				min = fileValue
			if fileValue > max:
				max = fileValue
		
		if len(curFiles) == 10:
			print( 'Comments directory is full' )
			webfileutils.move('test','old',str(min) + '.html')
		webfileutils.create(str(max+1) + '.html',text,'test')
		return True

	def get():
		"""Fetch all the current comments for display"""
		pass
	
	def delete(name):
		"""Allow access to remove an unwanted comment"""
		pass
