Feature: Movie Feature

  Scenario: Verify Movie Title and Rating for Inception
    Given the user is on the main movie page
    When the user searches for the movie "Inception"
    And opens the first search result
    Then the user should be redirected to the "Origen" movie page
    And the movie title displayed must be "Origen"
    And the movie rating must be "8,8"