from flask import Flask, jsonify
import magma

app = Flask(__name__)

BOOKS = [{
  "Tastament": "Old",
  "Titles": "12",
}, {
  "Testament": "New",
  "Titles": "16"
}]


@app.route("/")
def home():
  return "Biblia Leo Verson 0.1"


@app.route("/api/books/")
def bible_books():
  return jsonify(BOOKS)

@app.route("/cheka")
def lough():
  return magma.cheka()

@app.route("/lia")
def cry():
  return magma.lia()
  
if __name__ == "__main__":
  app.run("0.0.0.0", debug=True)
