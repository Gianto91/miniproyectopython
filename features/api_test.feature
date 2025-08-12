Feature: Prueba API de usuarios

  Scenario: Obtener usuario existente
    Given la API base es "https://reqres.in/api"
    When hago una solicitud GET a "/users/2"
    Then el código de respuesta debe ser 200
    And el campo "data.first_name" debe ser "Janet"
