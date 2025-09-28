# TEST CASES — API (SWAPI)

- GET /people/1/: 200 e name='Luke Skywalker'
- GET /people?search=luke: 200, count>=1, name contém 'Luke'
- GET /people/9999/: 404
- GET /planets/1/: 200 e name='Tatooine'
- GET /starships/9/: 200