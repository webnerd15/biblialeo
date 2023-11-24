from flask import Flask, jsonify
from flask_cors import CORS
import db, random

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
  return "Biblia Leo Verson 0.1"


@app.route("/api/en/<book>/<chapter>/<verse>")
def bible_books(book,chapter,verse):
  return jsonify(db.get_a_verse(book,chapter,verse))

@app.route("/api/en/verselinestoday/<lines>")
def verse_today(lines):
  if(int(lines)>=1):
    return jsonify(db.get_random_verse(int(lines)))
  else:
    return jsonify(db.get_random_verse(random.randint(1,10)))
  
@app.route("/api/en/versetoday/")
def verse_today_free():
    return jsonify(db.get_random_verse(random.randint(1,10)))
  
if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
