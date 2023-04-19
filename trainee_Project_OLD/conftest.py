import pytest
from appium import webdriver
from environment import desired_capabilities_catalog, desired_capabilities_buyiphone
from functions.buy_iphone import Byiphone
from functions.ui_catalog import UiCatalog, CheckPrompt

config = {
    'uicatalog': (desired_capabilities_catalog, UiCatalog),
    'check_prompt': (desired_capabilities_catalog, CheckPrompt),
    'buyiphone': (desired_capabilities_buyiphone, Byiphone)
}
# Мне нужно узнать как получить из конфига капабилитиз и класс
# А в фикстуре распаквать кортеж капабилитиз и класс, передать капабилитиз в драйвер
# а инстанс класса вызвать и вернуть. Без ретерн. (дложно что-то другое быть)
# Зачем закрывать драйвер

@pytest.fixture()
def driver(request):
    which_app = request.node.get_closest_marker("which_app").args[0]
    cap, instance = config[which_app]
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cap)
    driver.implicitly_wait(20)
    yield instance(driver)
    driver.quit()

