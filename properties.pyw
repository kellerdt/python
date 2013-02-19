#!c:/Python33 python

import os.path

class Cache:
	cache = {}

	def load(dir, name):
		""" Loads all of the properties from a file into the property cache """
		name = name + '.properties'
		file = os.path.join(dir, name)
		if os.path.exists(file):
			file = open(file, 'r')
			property = file.readline()
			while not property == '': # Last line will return empty string
				name = property[0:property.find('=')]
				value = property[property.find('=')+1:]
				Cache.set(name, value[:-1]) # Remove /n from the value
				property = file.readline()
			return True
		return False
		
	def set(name, value):
		""" Sets a particular value within the property cache """
		Cache.cache[name] = value
	
	def get(name):
		""" Fetches a value from the property cache """
		try:
			value = Cache.cache[name]
		except KeyError:
			value = ''
		return value