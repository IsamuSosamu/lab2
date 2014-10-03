import sqlite3


def statementToExecute(sql):
	dbconnection = sqlite3.connect('posts.db')
	conn = dbconnection.cursor()
	conn.execute(sql)
	dbconnection.commit()
	dbconnection.close()
class Post:
	def __init__(self):
		self.name = ''
		self.text = 0
class PostsOperations:
	def __init__(self):
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		conn.execute('create table if not exists posts (name text, words text)')
	def GetPosts():
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		conn.execute('select * from posts')
		return conn.fetchclone()
	def AddPost(name, text):
		dbconnection = sqlite3.connect('posts.db')
		conn = dbconnection.cursor()
		conn.execute('insert into posts(name,words) values '+str(name)+','+str(text))
