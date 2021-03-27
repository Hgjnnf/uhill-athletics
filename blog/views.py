from django.shortcuts import render
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .forms import BlogPostModelForm, BlogPostUpdateForm
from .models import BlogPost

def blog_post_list_view(request):
    qs = BlogPost.objects.all().published()
    template_name = 'blog/list.html'
    context = {'object_list':qs}
    return render(request, template_name, context)

@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = BlogPostModelForm()
    template_name = 'form.html'
    context = {'form':form}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save() 
    else:
        print(form.non_field_errors)
        print(form.is_bound)
    template_name = 'blog/updateform.html'
    context = {"title": f"Update {obj.title}", "form":form}
    return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'blog/delete.html'
    if request.method == "POST":
        obj.delete()
        return redirect("/blog")
    context = {"object":obj}
    return render(request, template_name, context)

