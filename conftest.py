from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.action_chains import ActionChains


caps = {}
caps["appium:platformName"] = "Android"
caps["appium:deviceName"] = "test"
caps["appium:app"] = "C:\\Users\\elushchikova\\Downloads\\app-kbrTest-debug (21).apk"
caps["appium:newCommandTimeout"] = 36000
caps["appium:connectHardwareKeyboard"] = True

driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
driver.implicitly_wait(500000)

def click (a:str,b:str):
    driver.find_element(by=a, value=b).click()

# Клики по элементам
def OnboardingGestAgeClick():
        click(AppiumBy.ID,"ru.mobiledimension.kbr:id/guestAgeBtn")
def AgreementCheckBoxClick():
        click(AppiumBy.ID,"ru.mobiledimension.kbr:id/agreementCheckBox")
def SaveButtonClick():
        click(AppiumBy.ID,"ru.mobiledimension.kbr:id/saveButton")
def Button1Click():
        click(AppiumBy.ID,"android:id/button1")


#Тут отдельно клик на элементы по XPATH, надо попросить добавить локаторы
def SkipAuthorizationClick():
    driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View[5]/android.widget.Button").click()
def SkipPopUpClick():
    driver.find_element(by=AppiumBy.XPATH,value="/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]").click()

#Класс с методами для скролла пикера на онбординге
class PickerScroll():
    def weekWheelPickerScroll(x: int, y: int):
        weekWheelPicker = driver.find_element(by=AppiumBy.ID, value="ru.mobiledimension.kbr:id/weekWheelPicker")
        ActionChains(driver).drag_and_drop_by_offset(source=weekWheelPicker, xoffset=x, yoffset=y).perform()

    def dayWheelPickerScroll(x: int, y: int):
        dayWheelPicker = driver.find_element(by=AppiumBy.ID, value="ru.mobiledimension.kbr:id/dayWheelPicker")
        ActionChains(driver).drag_and_drop_by_offset(source=dayWheelPicker, xoffset=x, yoffset=y).perform()

