from random import *

class Flashcards():
	def __init__(self):
		hello = self
	
	def cards(self, key_list, value_list):
		self.keys = key_list
		self.values = value_list
	
	def shuffle_cards(self, key_list, value_list):
		self.shuffledKeys = key_list
		self.shuffledValues = value_list
		index_shuf = range(len(key_list))
		shuffle(index_shuf)
		for i in index_shuf:
			self.shuffledKeys.append(key_list[i])
			self.shuffledValues.append(value_list[i])
		return self.shuffledKeys, self.shuffledValues
	
	def operate(self, key_list, value_list):
		self.cards(key_list, value_list)
		self.shuffle_cards
		
	def getShuffledKeys(self):
		return self.shuffledKeys
	
	def getShuffledValues(self):
		return self.shuffledValues
	
	def setShuffledKeys(self, key_list):
		self.shuffledKeys = key_list
	
	def setShuffledValues(self, value_list):
		self.shuffledValues = value_list
		
		
		