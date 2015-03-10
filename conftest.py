def pytest_configure(config):
    config.option.app_package = 'me.everything.magnetodemo'
    config.option.app_activity = 'me.everything.magnetodemo.Calculator'
    config.option.apk_path = config.getoption('--apk-path') or 'calc.apk'