from django.http import HttpResponse
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Group, User

def authirized(func):
          def check_user(request,*args, **kwargs):
                    if request.user.is_authenticated:
                              return func(request, *args, **kwargs)
                    return redirect('/auth/login/')
          return check_user

def index(request):
          template = 'index.html'
          posts = Post.objects.all().order_by('-pub_date')
          paginator = Paginator(posts, 10)
          page_number = request.GET.get('page')
          page_obj = paginator.get_page(page_number)
          contex = {'page_obj': page_obj, "paginator":paginator}
          return render(request, template, contex)
          
def group_posts(request, slug):
          template = 'group_list.html'
          group = get_object_or_404(Group, slug=slug)
          posts = Post.objects.all().filter(group=group).order_by('-pub_date')
          paginator = Paginator(posts, 10)
          page_number = request.GET.get('page')
          page_obj  =paginator.get_page(page_number)
          contex = {'group': group,
                    'page_obj': page_obj,
                    'paginator': paginator}
          return render(request, template, contex)

def profile(request, username):
          author = get_object_or_404(User, username=username)
          posts = Post.objects.all().filter(author=username).order_by('-pub_date')
          paginator = Paginator(posts, 5)
          page_number = request.GET.get('page')
          page_obj  = paginator.get_page(page_number)
          context = {'author': author,
                     'posts': posts,
                     'page_obj': page_obj,
                     'paginator': paginator}
          return render(request, 'profile.html', context)
def post_detail():
          context={}
          return render(request, 'post_detail.html', context)

