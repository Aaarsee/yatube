from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post, Group
def index(request):
          template = 'index.html'
          posts = Post.objects.order_by('-pub_date')[:10]
          contex = {'posts': posts}
          return render(request, template, contex)
          
def group_posts(request, slug):
          template = 'group_list.html'
          group = get_object_or_404(Group, slug=slug)
          posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
          contex = {'group': group,
                    'posts': posts,}
          return render(request, template, contex)


