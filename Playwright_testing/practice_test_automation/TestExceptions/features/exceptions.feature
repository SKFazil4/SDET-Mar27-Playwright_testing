Feature: Test Exceptions
  Scenario: Checking Row 2 Added
    Given practice page
    When user click "Add" button
    Then verify row 2 input field is displayed

  Scenario:  Checking added text is visible
    Given practice page
    When user click "Add" button
    When user type text "ReactJS" into "row2" row
    When user click on save button of "row2" row
    Then verify "ReactJS" text saved on "row2" row

  Scenario:  Checking text change in row 1
    Given practice page
    When user click "Edit" button
    When user type text "ReactJS" into "row1" row
    When user click on save button of "row1" row
    Then verify "ReactJS" text saved on "row1" row

  Scenario: Finding instructions text element
    Given practice page
    Given the "instructions" text element
    When user click "Add" button
    Then the "instructions" text should be invincible

   Scenario: Raising Timeout Exception
     Given practice page
     When user click "Add" button
     Then wait for 3 seconds and verify second input visibility
