import sqlite3
from model import *

modelInstance = PostsOperations()
modelInstance.AddPost("hurr""durr")
statementToExecute('insert into posts values (`1`,`2`)')
print(modelInstance.GetPosts())