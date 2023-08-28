from appium.webdriver.common.appiumby import AppiumBy
from conftest import OnboardingGestAgeClick, PickerScroll, AgreementCheckBoxClick, SaveButtonClick, SkipPopUpClick, \
    Button1Click, SkipAuthorizationClick, driver

# Прохождение онбординга через срок беременности со сроком 13 недель 5 дней
def test_1():
    OnboardingGestAgeClick()
    PickerScroll.weekWheelPickerScroll(x=0, y=-1170)
    PickerScroll.dayWheelPickerScroll(x=0, y=180)
    AgreementCheckBoxClick()
    SaveButtonClick()
    SkipPopUpClick()
    Button1Click()
    SkipAuthorizationClick()
    currentTermTextViewText=driver.find_element(by=AppiumBy.ID,value="ru.mobiledimension.kbr:id/currentTermTextView").get_attribute(name="text")
    beforeBirthTextVieText=driver.find_element(by=AppiumBy.ID,value="ru.mobiledimension.kbr:id/beforeBirthTextView").get_attribute(name="text")
    childBirthDayTextViewText=driver.find_element(by=AppiumBy.ID,value="ru.mobiledimension.kbr:id/childBirthDayTextView").get_attribute(name="text")
    assert childBirthDayTextViewText == ("28")
    assert currentTermTextViewText==("13 weeks and 5 days")
    assert beforeBirthTextVieText==("26 weeks and 2 days")
