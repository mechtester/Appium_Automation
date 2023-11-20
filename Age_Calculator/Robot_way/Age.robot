*** Settings ***
Library  AppiumLibrary
Test Teardown  Close Application

*** Test Cases ***
Test Case Name
    Open Application    http://0.0.0.0:4723/wd/hub    platformName=Android    appium:deviceName=7adf3fc7    appium:platformVersion=13.0    appium:appPackage=com.happyverse.agecalculator    appium:appActivity=com.configureit.core.MainActivity    appium:ensureWebviewsHavePages=${True}    appium:nativeWebScreenshot=${True}    appium:newCommandTimeout=${3600}    appium:connectHardwareKeyboard=${True}
    ${el1} =  Set Variable  id=com.happyverse.agecalculator:id/BUTTON5
    Click Element  ${el1}
    ${el2} =  Set Variable  xpath=(//android.widget.ImageView[@resource-id="com.happyverse.agecalculator:id/IMAGE_VIEW83"])[1]
    Click Element  ${el2}
    ${el3} =  Set Variable  id=com.happyverse.agecalculator:id/YourName
    Input Text  ${el3}  13-03-1996
    ${el4} =  Set Variable  id=com.happyverse.agecalculator:id/BUTTON6
    Click Element  ${el4}
    ${el5} =  Set Variable  id=com.happyverse.agecalculator:id/IMAGE_VIEW2
    Click Element  ${el5}
    ${el6} =  Set Variable  id=com.happyverse.agecalculator:id/YourName
    Input Text  ${el6}  13-03-1997
