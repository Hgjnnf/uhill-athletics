from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
    template_name = 'home.html'
    context = {}
    return render(request, template_name, context)