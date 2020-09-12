from django.shortcuts import render
from datetime import datetime
from random import randint

from .models import Event, DateCollect

from historian.utils import get_full_date, get_month_and_day
from historian.historian import Historian

historian = Historian()


def create_date():
    if not DateCollect.objects.filter(date=datetime.today()).exists():
        DateCollect.objects.create(date=datetime.today())


def store_events():
    date = datetime.today()
    if not DateCollect.objects.get(date=date).stored:
        events = historian._clean_events()
        for event in events:
            Event.objects.create(date=datetime.today(), event=event, used=False)
    dc = DateCollect.objects.get(date=date)
    dc.stored = True
    dc.save()


def get_random_event():
    today = datetime.today()
    events = Event.objects.filter(date=today)
    select = randint(0, len(events) - 1)

    return events[select]


def split_year_event(collection):
    events = list()
    for item in collection:
        text = item.event.split(" ")
        year = text[0]
        event = text[2:]
        event = " ".join(event)
        year_events = list()
        year_event = {"year": year, "event": event}
        events.append(year_event)
    return events


def index(request):
    create_date()
    store_events()

    event = get_random_event()

    context = {
        "today": get_full_date(),
        "event": event,
    }
    return render(request, "pages/index.html", context)


def table(request, day):
    if day != get_month_and_day():
        return render(request, "pages/error.html")
    today = datetime.today()
    collection = Event.objects.filter(date=today)

    events = split_year_event(collection)
    print(events)
    context = {
        "events": events,
    }
    return render(request, "pages/today.html", context)