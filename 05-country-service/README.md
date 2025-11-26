## 05-country-service
**Problem:**

In this exercise, you're tasked with writing a small RESTful API service that fetches data from another system.

This service should fetch data from the following third-party endpoints:
- https://restcountries.com/v3.1
- https://api.chucknorris.io

There should be the following endpoints:

``
GET /info/{country_name}
``

This endpoint fetches the name, capital, languages, borders and continents from a given country.

``
GET /status
``

This endpoint fetches the status of both endpoints, the version, uptime and a random Chuck Norris quote.

``
GET /
``

This endpoint returns a default message.

**Learning Outcome:**

By completing this exercise, you will:
- Understand the client-server architecture
- Understand how to write basic REST APIs
- Learn to write modular code