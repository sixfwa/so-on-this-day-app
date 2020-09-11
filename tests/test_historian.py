import unittest
import requests
from bs4 import BeautifulSoup

from scraper.utils import get_month_and_day as _get_month_and_day
from scraper.historian import Historian


class HistorianTest(unittest.TestCase):
    def setUp(self):
        self.historian = Historian()

    def test_todays_page(self):
        URL = f"https://en.wikipedia.org/wiki/{_get_month_and_day()}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        assert self.historian._todays_page() == soup