## I-reporter-api
### Build status 
[![Build Status](https://travis-ci.org/sammashar56/I-reporter-api.svg?branch=ch-tests-162302900)](https://travis-ci.org/sammashar56/I-reporter-api) [![Coverage Status](https://coveralls.io/repos/github/sammashar56/I-reporter-api/badge.svg?branch=develop)](https://coveralls.io/github/sammashar56/I-reporter-api?branch=develop) [![Maintainability](https://api.codeclimate.com/v1/badges/ec42c05ecbd4ede370b4/maintainability)](https://codeclimate.com/github/sammashar56/I-reporter-api/maintainability)
This is a corruption reporting app.

## Getting started

To get started I-reporter you will have clone ireporter repo.

Mac OS/Unix:

```bash 
$ git clone https://github.com/sammashar56/I-reporter-api.git
```

Windows:
* You will have to download git tool in this url [https://git-scm.com/download/win](https://git-scm.com/download/win)

* Ensure you follow the recommended settings

* Open git bash and type this command

```bash
$ git clone https://github.com/sammashar56/I-reporter-api.git
```

## Endpoints for v1 (memory storage version)

| HTTP VERB | API ROUTE | FUNCTION |
|-----------|-----------|----------|
|GET|`/api/v1/incidents`|Fetch all incidents|
|POST|`/api/v1/incidents`|Create an incident|
|GET|`/api/v1/incident/<int:id>`|Fetch a specific incident|
|PUT|`/api/v1/incident/<int:id>`|Update an incident|
|Delete|`/api/v1/incident/<int:id>`|Delete a specific product|

## Testing 

* Ensure you have postman installed in your computer.
* Test using this heroku link 
```
https://i-reporter-api.herokuapp.com/
```
