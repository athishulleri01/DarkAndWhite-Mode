from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Posts
# Create your views here.

class PostListView(ListView):
    model = Posts
    template_name = 'posts/main.html'
    
    
class PostDetailView(DetailView):
    model = Posts
    template_name = 'detail.html'
    

def PostViewListing(request):
    return render(request,'posts/main.html')