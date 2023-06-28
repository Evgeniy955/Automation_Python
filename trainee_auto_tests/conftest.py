import pytest
from appium import webdriver
from selene.support.shared import browser

from environment import options_catalog, chrome_options, DESIRED_CAPS_IOS_2, DESIRED_CAPS_IOS, DESIRED_CAPS_iPad
# from functions_ipad.buy_iphone import Byiphone
from functions.ui_catalog import UiCatalogAndroid, CheckPrompt, UiCatalogiOS, UiCatalogiPad
from selene import Browser, Config


config = {
    'uicatalog': (options_catalog, UiCatalogAndroid),
    'check_prompt': (options_catalog, CheckPrompt),
    # 'buyiphone': (chrome_options, Byiphone),
    'ios_uicatalog': (DESIRED_CAPS_IOS, UiCatalogiOS)
}

pytest_plugins = ['iPad_BDD.date_picker_iPad.date_picker_iPad']

# Мне нужно узнать как получить из конфига капабилитиз и класс
# А в фикстуре распаквать кортеж капабилитиз и класс, передать капабилитиз в драйвер
# а инстанс класса вызвать и вернуть. Без ретерн. (дложно что-то другое быть)
# Зачем закрывать драйвер

@pytest.fixture()
def mobile(request):
    which_app = request.node.get_closest_marker("which_app").args[0]
    cap, instance = config[which_app]
    browser_instance = Browser(Config(
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=cap),
        timeout=20,
    ))
    browser.config.driver = browser_instance.driver
    yield instance
    browser_instance.quit()


@pytest.fixture()
def browser_catalog(request):
    cap = DESIRED_CAPS_iPad
    instance = UiCatalogiPad
    browser_instance = Browser(Config(
        driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=cap),
        timeout=20,
    ))
    browser.config.driver = browser_instance.driver
    yield instance
    browser_instance.quit()