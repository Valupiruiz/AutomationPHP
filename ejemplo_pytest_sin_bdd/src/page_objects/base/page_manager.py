from src.factory.page.factory import PageFactory


class PageManager(object):

    def __init__(self, factory: PageFactory):
        self.factory = factory
        self.factory.observer.subscribe(self)
        self._page = None
        self._page_history = {}

    def __getattr__(self, name):
        attr = getattr(self._page, name)

        if not callable(attr):
            return attr

        def wrapper(*args, **kwargs):
            return attr(*args, **kwargs)

        return wrapper

    def update(self):
        self.page = self.factory.create_from(self._page)

    def create_with_name(self, name, refresh=False):
        self.page = self.factory.create_with_name(name, refresh)

    def set_active_driver(self, driver):
        if self.page is not None:
            self._page_history[self.factory.driver] = self._page

        self.factory.switch_driver(driver)
        if driver in self._page_history.keys():
            self.page = self._page_history[driver]
        else:
            self.page = self.factory.get_login()

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, new_page):
        del self._page
        self._page = new_page

