*** Settings ***
Library          RequestsLibrary
Library          Collections
Library          ../libraries/api_validators.py
Resource         ../resources/variables.robot

*** Keywords ***
Create API Session
    [Documentation]     Create a session to the JSONPlaceholder API.
    Create Session    jsonapi    ${BASE_URL}    headers=${EMPTY}    verify=True

Get All Users
    [Documentation]     Get a list of all users from the API.
    ${Response}=    GET On Session    jsonapi    /users
    RETURN    ${Response}

Get User By ID
    [Documentation]     Get a user by their ID.
    ${Response}=    GET On Session    jsonapi    /posts/1
    RETURN    ${Response}

Create New Post
    [Documentation]     Create a new post for a user.
    [Arguments]    ${user_id}    ${title}    ${body}
    ${payload}=    Create Dictionary    userId=${user_id}    title=${title}    body=${body}
    ${Response}=    POST On Session    jsonapi    /posts    json=${payload}
    RETURN    ${Response}
