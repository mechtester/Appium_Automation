from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
import time
from selenium.webdriver.common.by import By
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


desired_caps = {
  "platformName": "Android",
  "appium:deviceName": "7adf3fc7",
  "appium:platformVersion": "12.0",
  "appPackage": "com.miui.calculator",
  "appActivity": "com.miui.calculator.cal.CalculatorActivity"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
time.sleep(4)

wait=WebDriverWait(driver, 30)

## from appium.webdriver.common.touch_action import TouchAction
## create a TouchAction object
# touch_action = TouchAction(driver)
## simulate touch actions
# touch_action.press(x=118, y=1845).wait(100).release().perform()
# touch_action.press(x=395, y=1857).wait(100).release().perform()
# touch_action.press(x=433, y=1639).wait(100).release().perform()
# touch_action.press(x=929, y=2164).wait(100).release().perform()


time.sleep(30)
# from selenium.webdriver.common.by import By
# driver.find_element(By.ID, "com.miui.calculator:id/btn_9_s").click()

# from appium.webdriver.common.appiumby import AppiumBy
# driver.find_element(AppiumBy.ID,"com.miui.calculator:id/btn_9_s").click()

# from appium.webdriver.common.mobileby import MobileBy
# driver.find_element(MobileBy.ID,"com.miui.calculator:id/btn_9_s").click()


# from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# elementA = wait.until(
#     EC.element_to_be_clickable((MobileBy.ID, "com.miui.calculator:id/btn_9_s"))
# )
# elementA.click()


# Tap using bounds
# driver.tap([(168,2088),(912,2177)],10)


## Creating Xpath from text (Custom Made)
# english=wait.until(EC.element_to_be_clickable((By.XPATH, "//android.widget.TextView[contains(@text,'English')]")))
# english.click()


