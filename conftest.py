import os

calc_apk = os.path.abspath(os.path.join(os.path.dirname(__file__), 'calc.apk'))

def pytest_configure(config):
    config.option.app_package = 'me.everything.magnetodemo'
    config.option.app_activity = 'me.everything.magnetodemo.Calculator'
    config.option.apk_path = config.getoption('--apk-path') or calc_apk
    config.option.clean_install = True
