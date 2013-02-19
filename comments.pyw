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
		properties.Cache.load('c:/code/python','comments')
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
		
		if len(curFiles) == properties.Cache.get('numComments'):
			webfileutils.move('test','old',str(min) + '.html')
		webfileutils.create(str(max+1) + '.html',text,'test')
		return True

	def get():
		"""Fetch all the current comments for display"""
		properties.Cache.load('c:/code/python','comments')
		baseDir = os.path.join(properties.Cache.get('baseDir'),'test')
		
		results = {}
		files = os.listdir(baseDir)
		for file in files:
			content = open(os.path.join(baseDir,file), 'r').read()
			results[file] = content
		return results
	
	def delete(name):
		"""Allow access to remove an unwanted comment"""
		properties.Cache.load('c:/code/python','comments')
		testDir = os.path.join(properties.Cache.get('baseDir'),'test')
		oldDir = os.path.join(properties.Cache.get('baseDir'),'old')
		filename = name + '.html'
		if os.path.exists(os.path.join(testDir,filename)):
			webfileutils.remove(testDir, filename)
		elif os.path.exists(os.path.join(oldDir,filename)):
			webfileutils.remove(oldDir, filename)
		return True
