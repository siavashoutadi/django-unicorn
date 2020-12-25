from datetime import datetime
from typing import Optional

from django.utils.timezone import now

from books.models import Book
from pydantic import BaseModel

from django_unicorn.components import UnicornField, UnicornView


class PublishDateField(UnicornField):
    def __init__(self, year):
        self.year = year


class BookField(UnicornField):
    def __init__(self):
        self.title = "Neverwhere"
        self.publish_date_field = PublishDateField(year=1996)
        self.publish_date = datetime(1996, 9, 16)


class PydanticBook(BaseModel):
    title = "American Gods"
    publish_date: Optional[datetime] = datetime(1996, 9, 16)


class ObjectsView(UnicornView):
    unicorn_field = BookField()
    pydantic_field = PydanticBook()
    dictionary = {"name": "dictionary", "nested": {"name": "nested dictionary"}}
    book = Book(title="The Sandman")
    books = Book.objects.all()

    date_example = now()

    def get_date(self):
        self.date_example = now()

    def set_dictionary(self, val):
        self.dictionary = val
