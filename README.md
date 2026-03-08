# Books API

This repository contains a small Flask application that exposes a simple **Books API**.

The API allows clients to retrieve, create, update, and delete books stored in memory.

## Project Structure

The repository follows a simple structure.

```
project/
│
├─ src/
│   └─ app.py
│
├─ tests/
│   └─ .gitkeep
│
└─ pytest.ini
```

The `src` folder contains the Flask application.

The `tests` folder is where automated tests can be added. The `.gitkeep` file ensures the directory is tracked by Git even when it is empty.

## Running the API

From the project root, start the server with:

```
py src/app.py
```

The server will start on port **5000**.

You can interact with the API using tools such as a browser, `curl`, or Postman.

Example request:

```
curl http://localhost:5000/books
```

## API Endpoints

The API exposes the following endpoints.

### Retrieve All Books

```
GET /books
```

Returns a list of books stored by the server.

Example response:

```
[
  {"id": 1, "title": "Dune", "author": "Frank Herbert"},
  {"id": 2, "title": "The Hobbit", "author": "J.R.R. Tolkien"}
]
```

### Retrieve a Single Book

```
GET /books/{id}
```

Returns the book with the specified ID.

If the book does not exist, the server returns:

```
404 Not Found
```

### Create a Book

```
POST /books
```

Creates a new book.

Example request body:

```
{
  "title": "Neuromancer",
  "author": "William Gibson"
}
```

Successful requests return:

```
201 Created
```

If required fields are missing, the server returns:

```
400 Bad Request
```

### Update a Book

```
PUT /books/{id}
```

Updates an existing book.

If the book does not exist, the server returns:

```
404 Not Found
```
### Delete a Book

```
DELETE /books/{id}
```

Deletes the specified book.

Successful deletion returns:

```
204 No Content
```

If the book does not exist, the server returns:

```
404 Not Found
```

## Notes

The API stores data **in memory**, meaning the book list resets whenever the server restarts. This keeps the project simple and avoids introducing databases at this stage.
