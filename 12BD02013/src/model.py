import sqlite3


class Post():
	def __init__(self):
		self.name = ''
		self.text = 0
	def __str__(self):
		return self.name+" "+self.text
class PostsOperations:
	def __init__(self):
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		conn.execute('create table if not exists posts (name text, words text)')
		dbconnection.commit()
		dbconnection.close()
	def GetPosts(self):
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		list = []
		for row in conn.execute('select * from posts'):
			a = Post()
			a.name = row[0]
			a.text = row[1]
			list.append(a)
		return list
	def addPost(self,name, text):
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		data = [(name,text),]
		conn.executemany('insert into posts(name,words) values(?,?)', data)
		dbconnection.commit()
		dbconnection.close()
	def GetAbout(self):
		return "This is lab 2"