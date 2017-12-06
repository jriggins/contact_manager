*** Settings ***
Library  ContactManager

*** Variables ***

*** Keywords ***

no users
  clear all users

user ${user} registers
  register user  ${user}

user ${user} exists
  user should exist  ${user}

user ${user} can log in
  log in  ${user}
  ${user}=  logged in user
  should be equal as strings  user1  ${user.user_name}


*** Test Cases ***

User1 Can Register
  Given no users
  When user user1 registers
  Then user user1 exists


User1 Can Register and Login
  Given no users
  When user user1 registers
  Then user user1 can log in
