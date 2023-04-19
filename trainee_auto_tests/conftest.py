import pytest
from appium import webdriver
from environment import options_catalog, chrome_options
from functions.buy_iphone import Byiphone
from functions.ui_catalog import UiCatalog, CheckPrompt
from selene import Browser, Config

config = {
    'uicatalog': (options_catalog, UiCatalog),
    'check_prompt': (options_catalog, CheckPrompt),
    'buyiphone': (chrome_options, Byiphone)
}


# Мне нужно узнать как получить из конфига капабилитиз и класс
# А в фикстуре распаквать кортеж капабилитиз и класс, передать капабилитиз в драйвер
# а инстанс класса вызвать и вернуть. Без ретерн. (дложно что-то другое быть)
# Зачем закрывать драйвер

@pytest.fixture()
def mobile(request):
    which_app = request.node.get_closest_marker("which_app").args[0]
    cap, instance = config[which_app]
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=cap)
    mobile = Browser(Config(
        driver=driver,
        timeout=20
    ))
    yield instance(mobile)
    driver.quit()
