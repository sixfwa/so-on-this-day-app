import requests
from bs4 import BeautifulSoup, element

from utils import get_month_and_day as _get_month_and_day


class Historian:
    def _todays_page(self):
        URL = f"https://en.wikipedia.org/wiki/{_get_month_and_day()}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")

        return soup

    def _event_heading(self):
        page = self._todays_page()
        return page.find(id="Events").find_parent("h2")

    def _unordered_list(self):
        sibling = self._event_heading()
        unordered_list = sibling.find_next_sibling("ul")
        collection = list()
        for item in unordered_list:
            collection.append(item)

        return collection

    def _list_of_events(self):
        collection = self._unordered_list()
        events = list()
        for item in collection:
            if not isinstance(item, element.NavigableString):
                events.append(item.text)

        return events

    def _single_space(self, text):
        clean_text = " ".join(text.split())
        return clean_text

    def _remove_footnote(self, text):
        clean_text = text.split()
        last_word = clean_text[-1]
        if "[" in last_word:
            last_word = last_word.split("[", 1)
            last_word = last_word[0]
            clean_text[-1] = last_word
        clean_text = " ".join(clean_text)
        return clean_text

    def _clean_events(self):
        events = self._list_of_events()
        clean_events = list()
        for event in events:
            clean_event = self._single_space(event)
            clean_event = self._remove_footnote(clean_event)
            clean_events.append(clean_event)

        return clean_events


historian = Historian()

for item in historian._clean_events():
    print(item)