*** Settings ***
Library  RPA.Browser.Playwright
Library    OperatingSystem
Library    Process

*** Variables ***
${URL}         https://robotsparebinindustries.com
${BROWSER}     chromium
${FIRSTNAME}   First!
${USERNAME}    maria
${PASSWORD}    thoushallnotpass
${LASTNAME}    Last!
${SALESRESULT}  1000
${RESULT}

*** Test Cases ***
Playwright: Open a browser in headless mode
    New Browser    ${BROWSER}    headless=True    
    New Page       ${URL}
    Type Text      input#username    ${USERNAME}
    Type Secret    input#password    $PASSWORD
    Click          button.btn-primary
    Type Text      input#firstname   ${FIRSTNAME}
    Type Text      input#lastname    ${LASTNAME}
    Type Text      input#salesresult    ${SALESRESULT}
    Click      button.btn-primary
    Click    button.btn.btn-info.btn-secondary
    ${RESULT}=    Get Text    span.performance     
    Log To Console   ${RESULT}
    Close Browser