*** Settings ***
Library  RPA.Browser.Playwright

*** Variables ***
${URL}  https://de.wikipedia.org/wiki/Wikipedia:Hauptseite
${BROWSER}  chromium
${FIRSTNAME}    
${USERNAME}  
${PASSWORD}    


*** Test Cases ***
Playwright: Open a browser in GUI mode
    ${FIRSTNAME}=     Set Variable    First!
    ${USERNAME}=     Set Variable    maria
    ${PASSWORD}=     Set Variable    thoushallnotpass
    
    Open Browser        
    # New Browser    ${BROWSER}    headless=False
    New Page    https://robotsparebinindustries.com
    Type Text    input#username    ${USERNAME}
    Type Secret    input#password    $PASSWORD
    Click    button.btn-primary
    Type Text    input#firstname    ${FIRSTNAME}
    