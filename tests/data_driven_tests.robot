*** Settings ***
Resource          ../resources/api_keywords.robot

*** Test Cases ***
Create User And Verify - Positive
    [Documentation]    Verify that a new user can be created and the response is correct.
    [Template]    Create User And Verify
    Title 1    This is the body for user 1.    1
    Title 2    This is the body for user 2.    2
    Title 3    This is the body for user 3.    3
*** Keywords ***
Create User And Verify
    [Documentation]    Create a new user and verify the response.
    [Arguments]    ${title}    ${body}    ${user_id}
    Create API Session
    ${response}=    Create New Post    ${user_id}    ${title}    ${body}
    Should Be Equal As Integers    ${response.status_code}    201
    Should Be Equal    ${response.json()['title']}    ${title}
    RETURN    ${response.json()}