Feature: Un pokemon ya elegido dice su habilidad
  Scenario: El pokemon elegido previamente dice su habilidad
     Given el "pokemon" fue elegido
      When elijo el modo "hablar"
      Then el sistema me dice su nombre y habilidad
