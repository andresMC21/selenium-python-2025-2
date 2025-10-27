Feature: Artist Feature

  Scenario: Verify Bruno Mars Latest Release Date
    Given the user is on the main page
    When he clicks the search button
    And the user types the artist name "Bruno Mars" and searches 
    And opens the first result
    Then the user should be redirected to "Bruno Mars music, videos, stats, and photos" page
    And his latest release date must be "3 October 2025"