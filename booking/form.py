from django import forms
from .choices import room_choices
from .models import BookingData
from django.forms import SelectDateWidget


class BookingModelForm(forms.ModelForm):
    class Meta:
        model = BookingData
        fields = ['first_name', 'last_name', 'email', 'room', 'date', 'book_from', 'book_until', 'comments']
        labels = {
            "first_name":"First Name*",
            "last_name":"Last Name*",
            "email":"Email Address*",
            "room":"Room*",
            "date":"Date*",
            "book_from":"Book From(24-hr format)*",
            "book_until":"Booking Until(24-hr format)*",
        }
        widgets = {
            'date': SelectDateWidget(empty_label=("Year", "Month", "Date")),
        }
        

    def clean_space(self, *args, **kwargs):
        room = self.cleaned_data.get('room')
        date = self.cleaned_data.get('date')
        book_from = self.cleaned_data.get('book_from')
        book_until = self.cleaned_data.get('book_until')
        qs_roomdate = BookingData.objects.filter(room = room, date = date)

        def validate_booking_time(*args, **kwargs):
            for bookdat in BookingData.objects.all():
                bookf = bookdat.book_from
                booku = bookdat.book_until
                if booku > book_until > bookf or booku > book_from > bookf:
                    return True
                elif book_until >= booku and book_from <= bookf:
                    return True

        if qs_roomdate.exists() and validate_booking_time():
            return False
        return room, date, book_from, book_until





