*** Settings ***
Resource          ../resources/api_keywords.robot

*** Test Cases ***
Test Get All Users - Positive
    [Documentation]    Verify that all users can be retrieved from the API.
    Create API Session
    ${Response}=    Get All Users
    Should Be Equal As Integers    ${Response.status_code}    200
    Length Should Be    ${Response.json()}    10

Test Get User By ID - Validate payload
    [Documentation]    Verify that a user can be retrieved by their ID and the payload is
    Create API Session
    ${Response}=    Get User By ID
    Should Be Equal As Integers    ${Response.status_code}    200
    Dictionary Should Contain Key    ${Response.json()}    title

Test Create New Post - Positive
    [Documentation]    Verify that a new post can be created for a user.
    Create API Session
    ${Response}=    Create New Post    1    Test Title    This is a test body.
    Should Be Equal As Integers    ${Response.status_code}    201
    Should Be Equal    ${Response.json()['title']}    Test Title

Negative Test - Invalid Endpoint
    [Documentation]    Verify that accessing an invalid endpoint returns a 404 status code.
    Create API Session
    ${Response}=    GET On Session    jsonapi    /invalid    expected_status=404    
    Should Be Equal As Integers    ${Response.status_code}    404