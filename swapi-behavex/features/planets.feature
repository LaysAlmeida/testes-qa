Feature: Planets (SWAPI)
  Scenario: GET /planets/1/ deve retornar Tatooine
    Given que defino o endpoint "/planets/1/"
    When eu faço uma requisição GET
    Then o status code deve ser 200
    And o campo "name" deve ter valor "Tatooine"