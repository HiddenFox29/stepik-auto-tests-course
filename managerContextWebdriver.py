class Webdriver():

    def __init__(self, driver) -> None:
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.driver.quit()