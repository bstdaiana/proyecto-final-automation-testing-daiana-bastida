"""
Fixture compartido 'driver' para todos los tests de UI, mas un hook
que toma un screenshot automatico cuando un test de UI falla.
Selenium 4 gestiona el ChromeDriver automaticamente (Selenium Manager),
no hace falta instalar nada aparte.
"""
import datetime
import os

import pytest
from selenium import webdriver

SCREENSHOTS_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "screenshots")
os.makedirs(SCREENSHOTS_DIR, exist_ok=True)


@pytest.fixture
def driver():
    drv = webdriver.Chrome()
    drv.maximize_window()
    yield drv
    drv.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Se ejecuta despues de cada fase del test. Si el test fallo durante
    la ejecucion y usa el fixture 'driver', guarda un screenshot con
    nombre descriptivo (nombre del test + fecha/hora).
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver_fixture = item.funcargs.get("driver")
        if driver_fixture is not None:
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_name = item.name.replace("[", "_").replace("]", "_").replace("/", "_")
            filename = f"{safe_name}_{timestamp}.png"
            filepath = os.path.join(SCREENSHOTS_DIR, filename)

            try:
                driver_fixture.save_screenshot(filepath)
                print(f"\nScreenshot guardado: {filepath}")
            except Exception as e:
                print(f"\nNo se pudo guardar el screenshot: {e}")