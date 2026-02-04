## 06-library-api
**Problem:**

As a continuation from *04-library*, your task is to implement a RESTful API service out of the library.
There should be the following endpoints:

``
GET /
``

This endpoint returns a default message.

``
GET /books
``

This endpoint fetches all books.

``
GET /books/{id}
``

This endpoint fetches information from a book with that ID. IDs should be generated using UUID4.

``
POST /books
``

Sending a valid HTTP request to this endpoint creates a book.

``
DELETE /books/{id}
``

This endpoint deletes a book with that ID.

``
PUT /books/{id}
``

Update the information of a book with that ID.

The service should be implemented with the Model-view-controller (MVC) pattern. Data may be stored inside the programme's runtime.

**Learning Outcome:**

By completing this exercise, you will:
- Understand the client-server architecture
- Understand how to write basic REST APIs
- Learn to write modular code