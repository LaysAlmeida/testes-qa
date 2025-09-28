Feature: Starships (SWAPI)
  Scenario: GET /starships/9/ deve retornar nave válida
    Given que defino o endpoint "/starships/9/"
    When eu faço uma requisição GET
    Then o status code deve ser 200