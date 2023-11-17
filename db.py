from sqlalchemy import create_engine, text
import os

engine = create_engine(os.environ['DB_CONNECTION_STRING'])
#dbc -> database_connection object
dbc = engine.connect()

#dbc.execute(text("CREATE TABLE IF NOT EXISTS example(id INTEGER, name VARCHAR(20))"))

#dbc.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
#dbc.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
#dbc.commit()
sql = "SELECT bible_kjv.text, bible_books_en.fullname, bible_kjv.chapter, bible_kjv.verse FROM bible_kjv LEFT JOIN bible_books_en ON bible_kjv.book = bible_books_en.number WHERE bible_kjv.book = 41 AND bible_kjv.chapter = 1 AND bible_kjv.verse= 1"

result = dbc.execute(text(sql))

for row in result.mappings():
  #print(row) 
  print("Verse:" , row["text"], row['fullname'], row['chapter'])