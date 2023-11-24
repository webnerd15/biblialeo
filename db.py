from sqlalchemy import create_engine, text
import os, random

engine = create_engine(
  os.environ['DB_CONNECTION_STRING'],
  connect_args={
    "ssl": {
      "ssl_ca":"/etc/ssl/cert.pem"
    }
  })
#dbc -> database_connection object
#dbc = engine.connect()

#dbc.execute(text("CREATE TABLE IF NOT EXISTS example(id INTEGER, name VARCHAR(20))"))

#dbc.execute(text("INSERT INTO example (name) VALUES (:name)"), {"name": "Ashley"})
#dbc.execute(text("INSERT INTO example (name) VALUES (:name)"), [{"name": "Barry"}, {"name": "Christina"}])
#dbc.commit()

#WHERE bible_kjv.book = :book AND bible_kjv.chapter = :chapter AND bible_kjv.verse= :verse"
'''
with engine.connect() as dbc:
  sql = "SELECT bible_kjv.text, bible_books_en.fullname, bible_kjv.chapter, bible_kjv.verse FROM bible_kjv LEFT JOIN bible_books_en ON bible_kjv.book = bible_books_en.number LIMIT 0,5"
  
  result = dbc.execute(text(sql))

  res_dict = []
  for row in result.all():
    print(row.fullname, row.chapter, row.verse, row.text)
    res_dict.append([{"Title":row.fullname, "Chapter":row.chapter, "Verse":row.verse, "Text":row.text
                     }])
    #res_dict.append(dict(row))
  print("===========================")
  print(res_dict)
  dbc.close()
'''

sql = "SELECT chapters FROM bible_books_en WHERE number = :book"
with engine.connect() as dbc:
  result = dbc.execute(text(sql),dict(book=2))
  chapters = result.first()[0]
  dbc.close()
  print(chapters)

def fetch_a_verse(book, chapter, verse):
  sql = "SELECT bible_kjv.text, bible_books_en.fullname, bible_kjv.chapter, bible_kjv.verse FROM bible_kjv LEFT JOIN bible_books_en ON bible_kjv.book = bible_books_en.number WHERE bible_kjv.book = :book AND bible_kjv.chapter = :chapter AND bible_kjv.verse= :verse"
  
  with engine.connect() as dbc:
    result = dbc.execute(text(sql),dict(book=book,chapter=chapter,verse=verse))
    res_dict = []
    for row in result.all():
      res_dict.append([{"Title":row.fullname, "Chapter":row.chapter, "Verse":row.verse, "Text":row.text}])
    dbc.close()
    
    return res_dict

def get_number_of_chapters(book):
  sql = "SELECT chapters FROM bible_books_en WHERE number = :book"
  with engine.connect() as dbc:
    result = dbc.execute(text(sql),dict(book=book))
    return result.first()[0]

def get_number_of_verses(book, chapter):
  sql = "SELECT COUNT(verse) AS verses FROM bible_kjv WHERE book = :book AND chapter = :chapter"
  with engine.connect() as dbc:
    result = dbc.execute(text(sql),dict(book=book,chapter=chapter))
    return result.first()[0]

def get_random_verse(number_of_lines):
  # get a random book from 66 books availble
  book = random.randint(1,66)
  # get number of chapters from the random chosen book
  chapters = get_number_of_chapters(book)
  # get a random chapter from the available chapters
  random_chapter = random.randint(1,chapters)
  # get number of verses from the random chosen chapter
  verses = get_number_of_verses(book, random_chapter)
  # get a random verse to start from the available verses
  start_verse = random.randint(1,verses)
  
  sql = "SELECT bible_kjv.text, bible_books_en.fullname, bible_kjv.chapter, bible_kjv.verse FROM bible_kjv LEFT JOIN bible_books_en ON bible_kjv.book = bible_books_en.number WHERE bible_books_en.number = :book AND bible_kjv.chapter = :chapter LIMIT :start_verse,:number_of_lines"
  
  with engine.connect() as dbc:
    result = dbc.execute(text(sql), dict(book=book,chapter=random_chapter,start_verse=start_verse,number_of_lines=number_of_lines))
    
    res_dict = []
    for row in result.all():
      res_dict.append([{"Title":row.fullname, "Chapter":row.chapter, "Verse":row.verse, "Text":row.text}])
    
    dbc.close()
    
    return res_dict
    
