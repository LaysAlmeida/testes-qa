Feature: People (SWAPI)
  Como QA
  Quero validar endpoints de pessoas
  Para assegurar disponibilidade e contrato

  Scenario: GET /people/1/ deve retornar Luke Skywalker
    Given que defino o endpoint "/people/1/"
    When eu faço uma requisição GET
    Then o status code deve ser 200
    And o campo "name" deve ter valor "Luke Skywalker"