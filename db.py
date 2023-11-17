from sqlalchemy import create_engine, text
import os 

db_user = os.environ['DB_USERNAME']
db_pass = os.environ['DB_PASSWORD']

connection_string = "mysql+mysqlconnector://"+db_user+":"+db_pass+"@aws.connect.psdb.cloud/bibledb"
engine = create_engine(connection_string)
connection = engine.connect()

connection.execute(text("CREATE TABLE IF NOT EXISTS example(id INTEGER, name VARCHAR(20))"))

#connection.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
#connection.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
#connection.commit()
sql = "SELECT bible_kjv.text, bible_books_en.fullname, bible_kjv.chapter, bible_kjv.verse FROM bible_kjv LEFT JOIN bible_books_en ON bible_kjv.book = bible_books_en.number WHERE bible_kjv.book = 40 AND bible_kjv.chapter = 1 AND bible_kjv.verse= 1"

result = connection.execute(text(sql))

for row in result.mappings():
  #print(row) 
  print("Verse:" , row["text"], row['fullname'], row['chapter'])