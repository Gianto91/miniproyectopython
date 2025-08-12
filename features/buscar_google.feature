Feature: Buscar en Google
  Scenario: Buscar la palabra "Python"
    Given que abro Google
    When busco "Python"
    Then el título de la página contiene "Python"
