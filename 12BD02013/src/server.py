import http.server
import socketserver
import sqlite3
from controller import *
from model import *
import sys
import os
from sys import version as python_version
from cgi import parse_header, parse_multipart

if python_version.startswith('3'):
    from urllib.parse import parse_qs
#import view

PORT = 8000
class myHandler(http.server.BaseHTTPRequestHandler):
	
	def parse_POST(self):
		ctype, pdict = parse_header(self.headers['content-type'])
		if ctype == 'multipart/form-data':
			postvars = parse_multipart(self.rfile, pdict)
		elif ctype=='application/x-www-form-urlencoded':
			length = int(self.headers['content-length'])
			postvars = parse_qs(
					self.rfile.read(length).decode('UTF-8'), 
					keep_blank_values=1)
		else:
			postvars = {}
		return postvars
	def loadTemplate(self,which):
			f = open(which,'r')
			content = ""
			for line in f.readlines():
				content += line
			f.close()
			content = content[content.find('<'):]
			return str(content)
	def do_POST(self):
		
		postvars = self.parse_POST()
		c = Controller()
		c.addPost(postvars['name'][0],postvars['text'][0])
		content = self.loadTemplate("index.html")
		toreplace = self.loadTemplate("add_post.html")
		content = content.replace("$$$CONTENT$$$",toreplace)
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(content,"UTF-8"))
	def do_GET(self):
		print(self.path)
		content = ""
		c = Controller()
		if self.path=="/" or self.path=="/index.html":
			content = self.loadTemplate("index.html")
			list1 = c.GetAllPosts()
			to_insert = self.loadTemplate("table_template.html")
			allposts = ""
			for i in range(len(list1)):
				table_content = self.loadTemplate("posts_template.html")
				table_content = table_content.replace("$NAME$",list1[i].name)
				table_content = table_content.replace("$TEXT$",list1[i].text)
				allposts += table_content
			to_insert = to_insert.replace("CONTENT",allposts)
			content = content.replace("$$$CONTENT$$$",to_insert)
		if self.path=="/about.html":
			content = self.loadTemplate("index.html")
			about_text = c.about()
			content = content.replace("$$$CONTENT$$$",about_text)	
		if self.path=="/add.html":
			content = self.loadTemplate("index.html")
			toreplace = self.loadTemplate("add_post.html")
			content = content.replace("$$$CONTENT$$$",toreplace)	
			
	#	print(self.query)
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		self.wfile.write(bytes(content,"UTF-8"))
		
httpd = socketserver.TCPServer(("", PORT), myHandler)

print ("serving at port", PORT)
httpd.serve_forever()

