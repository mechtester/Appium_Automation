*** Settings ***
Library    DataDriver    /home/vignesh/PycharmProjects/Appium_Automation/Age_Calculator/Robot_way/Test_data.xlsx    sheet_name=Sheet1
Library    AppiumLibrary
Suite Setup    Open App
Suite Teardown    Close Application

Test Template    Enter Date

*** Variables ***
${APPLICATION_URL}   http://0.0.0.0:4723/wd/hub
${DEVICE_NAME}       7adf3fc7
${PLATFORM_VERSION}  13.0
${APP_PACKAGE}       com.happyverse.agecalculator
${APP_ACTIVITY}      com.configureit.core.MainActivity

*** Test Cases ***
Test_1   ${date_input}


*** Keywords ***
Open App
    Open Application    ${APPLICATION_URL}    platformName=Android    appium:deviceName=${DEVICE_NAME}    appium:platformVersion=${PLATFORM_VERSION}    appium:appPackage=${APP_PACKAGE}    appium:appActivity=${APP_ACTIVITY}    appium:ensureWebviewsHavePages=${True}    appium:nativeWebScreenshot=${True}    appium:connectHardwareKeyboard=${True}
    ${el1} =    Set Variable    id=com.happyverse.agecalculator:id/BUTTON5
    Click Element    ${el1}
    ${el2} =    Set Variable    xpath=(//android.widget.ImageView[@resource-id="com.happyverse.agecalculator:id/IMAGE_VIEW83"])[1]
    Click Element    ${el2}

Enter Date
    [Arguments]    ${date_input}

    ${el3} =    Set Variable    id=com.happyverse.agecalculator:id/YourName
    Input Text    ${el3}    ${date_input}
    ${el4} =    Set Variable    id=com.happyverse.agecalculator:id/BUTTON6
    Click Element    ${el4}
    ${el5} =    Set Variable    id=com.happyverse.agecalculator:id/IMAGE_VIEW2
    Click Element    ${el5}



Kill App
    Close Application

