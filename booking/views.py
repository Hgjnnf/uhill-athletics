from django.shortcuts import render
from .form import BookingModelForm
from .models import BookingData
from django.contrib import messages

# Create your views here.
def book_form_view(request):
    form = BookingModelForm(request.POST or None)
    if form.is_valid() and form.clean_space():
        obj = form.save(commit=False)
        obj.save()
        form = BookingModelForm()
        messages.add_message(request, messages.INFO, "Your Form has been Recorded.")  
    elif form.is_valid() and form.clean_space() == False:
        messages.add_message(request, messages.ERROR, "Error: This room has been taken at this time, please try again!")
    template_name = 'bookingForm.html'
    context = { 
        'form': form
        }
    return render(request, template_name, context)

def existing_bookings_view(request):
    qs = BookingData.objects.all()
    context = {'object_list': qs}
    template_name = 'existBookList.html'
    return render(request, template_name, context)
        