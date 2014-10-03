import sqlite3
from model import *

class Controller:
	def __init__(self):
		self.modelInstance = PostsOperations()
	def GetAllPosts(self):
		return self.modelInstance.GetPosts()
	def addPost(self,name,text):
		self.modelInstance.addPost(name,text)
	def about(self):
		return self.modelInstance.GetAbout()
	