from flask import Flask, request

app = Flask(__name__)

# In-memory data store
books = [
    {"id": 1, "title": "Dune", "author": "Frank Herbert"},
    {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
]

next_book_id = 3

# GET /books
@app.route("/books", methods=["GET"])
def get_books():
    return books

# GET /books/1
@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] == book_id:
            return book

    return {"error": "Book not found"}, 404

# POST /books
@app.route("/books", methods=["POST"])
def create_book():
    global next_book_id

    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return {"error": "Missing required fields: title and author"}, 400

    book = {
        "id": next_book_id,
        "title": data["title"],
        "author": data["author"],
    }

    books.append(book)
    next_book_id += 1

    return book, 201

# PUT /books/1
@app.route("/books/<int:book_id>", methods=["PUT"])
def update_book(book_id):
    data = request.get_json()

    if not data or "title" not in data or "author" not in data:
        return {"error": "Missing required fields: title and author"}, 400

    for book in books:
        if book["id"] == book_id:
            book["title"] = data["title"]
            book["author"] = data["author"]
            return book

    return {"error": "Book not found"}, 404

# DELETE /books/1
@app.route("/books/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            return "", 204

    return {"error": "Book not found"}, 404

# Start server
if __name__ == "__main__":
    app.run(port=5000)