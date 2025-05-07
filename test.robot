*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${URL}  https://de.wikipedia.org/wiki/Wikipedia:Hauptseite
${BROWSER}  Chrome

*** Test Cases ***
Test Ladezeit und Seitenelemente
    Open Browser  ${URL}  ${BROWSER}
    Sleep    3s
    Close Browser