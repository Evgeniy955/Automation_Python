from appium import webdriver
from selenium.webdriver.common.by import By



desired_capabilities ={
    'platformName': "Android",
    'platformVersion': "13",
    'deviceName': "9A191FFAZ004MA",
    'appPackage': "org.wikipedia",
    'appActivity': "org.wikipedia.main.MainActivity",
    'app': "C:/Users/Yevhen/PycharmProjects/Automation/AppiumTests/app_wiki/wikipedia_2.7.50398.apk"
}


driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)

"""
XPATH 
"//android.widget.ImageView[@name='Search Wikipedia']"
"""

driver.implicitly_wait(5)

driver.find_element(By.ID, 'org.wikipedia:id/search_container').click()

e = driver.find_element(By.ID, "org.wikipedia:id/search_src_text")
e.clear()
e.send_keys("Python")

text = driver.find_element(By.ID, 'org.wikipedia:id/page_list_item_title').text


assert 'Python' in text, f'Expected Python to be {text}'
