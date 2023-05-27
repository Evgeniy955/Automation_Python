from appium import webdriver
from app.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        'platformName': "Android",
        'platformVersion': "11",
        'deviceName': "Android Emulator",
        'app': "C:/Users/halitsyn.y/PycharmProjects/AppiumTests/app_wiki/wikipedia_2.7.50398.apk"
    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(5)
    context.app = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
