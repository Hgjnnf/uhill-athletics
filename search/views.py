from django.shortcuts import render

# Create your views here.
from blog.models import BlogPost

from .models import SearchQuery

def search_view(request):
    query = request.GET.get('q', None)
    context={"query": query}
    if query is not None:
        SearchQuery.objects.create(query=query)
        blog_list = BlogPost.objects.search(query=query)
        context['blog_list'] = blog_list
    return render(request, 'search/view.html', context)