Feature: Prueba web de login

  Scenario: Validar login con credenciales válidas
    Given abro el navegador en la página de login
    When ingreso usuario "tomsmith" y contraseña "SuperSecretPassword!"
    Then debería ver el mensaje "You logged into a secure area!"
