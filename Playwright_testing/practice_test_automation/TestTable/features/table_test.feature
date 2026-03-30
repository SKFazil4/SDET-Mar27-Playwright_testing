Feature: Test Table
  Scenario: Language Filter
    Given practice page
    When user select "Java" language filter
    Then verify only "Java" language course available

  Scenario: Level Filter
    Given practice page
    When user unchecks "Intermediate" and "Advanced"
    Then verify only "Beginner" course available

  Scenario: Min enrollment filter
    Given practice page
    When user choose "10,000+" enrollment
    Then verify only "10000" or more enrollment courses available

  Scenario: Combined filters
    Given practice page
    When user select "Python" language filter
    When user unchecks "Intermediate" and "Advanced"
    When user choose "10,000+" enrollment
    Then the table data should consists only "Python", "Beginner" courses with "10000" enrollment

  Scenario: No result state
    Given practice page
    When user select "Python" language filter
    When user uncheck "Beginner"
    Then user should see "No matching courses." in "noData" id element

  Scenario: Reset button visibility and behaviour
    Given practice page
    When user select "Python" language filter
    When user changes anything "Reset" button appears
    And click "Reset" button
    Then verify all filters are reset
    And verify "Reset" button is hidden

  Scenario: Sort by enrollments
    Given practice page
    When user sets sort by to "Enrollments"
    Then verify visible rows are ordered by "Enrollments"

  Scenario: Sort by Course Name
    Given practice page
    When user sets sort by to "Course Name"
    Then verify visible rows are ordered by "Course Name"