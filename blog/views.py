# from django.shortcuts import render
from django.views.generic import ListView #추가
from .models import Post
from django.views.generic import ListView, DetailView



# Create your views here.

class PostList(ListView):
    model = Post
    ordering = '-pk' #추가
#추가
class PostDetail(DetailView):
    model = Post

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post':post,
        }

    )

