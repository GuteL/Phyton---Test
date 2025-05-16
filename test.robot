*** Settings ***
Library  RPA.Browser.Playwright
Library  OperatingSystem
Library  Process
Library    RPA.Browser.Selenium


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
    Click          text="Order your robot!"
    Click          button.btn.btn-dark 
    Click    css=select#head.custom-select
    Select Options By    css=select#head.custom-select    value    1   
    Click    input#id-body-4.form-check-input
    Type Text    css=input.form-control[placeholder="Enter the part number for the legs"]    2
    Type Text    css=input.form-control[placeholder="Shipping address"]     beispielstrasse 1
    Click    button#order.btn.btn-primary
    Take Screenshot
    