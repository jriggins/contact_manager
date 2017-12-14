
*** Settings ***

Library  ContactManager.py
Test Setup  Start App
Test Teardown  Stop App


*** Variables ***

*** Keywords ***

no users
  clear all users


user ${user} registers
  register user  ${user}


user ${user} exists
  user should exist  ${user}


user ${user} can log in
  ${response}=  log in  ${user}
  should be equal as strings  200  ${response.status_code}
  should not be empty  ${response.content}


user logs in with email ${email_address} and password ${password}
  ${response}=  log in2  ${email_address}  ${password}


login fails
  should be equal as strings  404  ${response.status_code}


*** Test Cases ***

User1 Can Register
  Given no users
  When user user1 registers
  Then user user1 exists


User1 Can Register and Login
  Given no users
  When user user1 registers
  Then user user1 can log in


Attempted Login with Invalid Credentials
  Given no users
  When user logs in with email bad@example.org and password BadPassword
  Then login fails
