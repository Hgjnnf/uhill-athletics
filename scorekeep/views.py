from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SelectSportForm, ScoreForm, ScoreUpdateForm
from .models import ScoreCreate

# Create your views here.
def ScoreListView(request):
    qs = ScoreCreate.objects.all()
    template_name = 'scorekeep/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

@staff_member_required
def SportsSelectView(request):
    form = SelectSportForm(request.POST or None)
    if form.is_valid():
        if form.cleaned_data['choice'] == 'BB':
            return redirect("/score/bbscore/")
        elif form.cleaned_data['choice'] == 'VB':
            return redirect("/score/vbscore/")
    template_name = 'scorekeep/sportsSelect.html'
    context = {
        "form": form
    }
    return render(request, template_name, context)

@staff_member_required
def BBScoreCreateFormView(request):
    form = ScoreForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        slug = obj.slug
        form = ScoreForm()
        return redirect(f"/score/bbscore/{slug}")
    template_name = 'scorekeep/scoreForm.html'
    context = {
        'form':form
    }
    return render(request,template_name,context)

@staff_member_required
def VBScoreCreateFormView(request):
    form = ScoreForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        slug = obj.slug
        form = ScoreForm()
        return redirect(f"/score/vbscore/{slug}")
    template_name = 'scorekeep/scoreForm.html'
    context = {
        'form':form
    }
    return render(request,template_name,context)


def ScoreDisplayUpdateView(request, slug, sport):
    obj = get_object_or_404(ScoreCreate, slug=slug)
    template_name = 'scorekeep/scoreDisplay.html'
    form = ScoreUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        "object": obj,
        "form": form,
        "sport": obj.sport,
        "bb": "BB",
        "vb": "VB",
    }
    return render(request, template_name, context)

@staff_member_required
def ScoreDeleteView(request, slug, sport):
    obj = get_object_or_404(ScoreCreate, slug=slug)
    template_name = 'scorekeep/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/score")
    context = {"object":obj}
    return render(request, template_name, context)











