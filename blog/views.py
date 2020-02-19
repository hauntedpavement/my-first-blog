from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

#posts in performing a query to create a list will return collection of objects that match
# the query, known as a Queryset

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


# in return render() we define a dictionary posts. the dictionary only has one entry, posts, to which we 
# assign our Quryset containing all projects. the posts dictionary is used to send information
# to your template