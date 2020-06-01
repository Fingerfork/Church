from django.shortcuts import render, redirect
from django.views.generic import View,FormView
from .models import Post,Tag
from .utils import *
from .forms import TagForm,PostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from .forms import UserRegistrationForm
from django.views.generic.base import TemplateView
class RegisterDoneView(TemplateView):
    template_name = 'blog/includes/registration_done.html'

#def register(request):
   # if request.method == 'POST':
      #  user_form = UserRegistrationForm(request.POST)
       # if user_form.is_valid():
          #  new_user = user_form.save(commit=False)
          #  new_user.set_password(user_form.cleaned_data['password'])
           # new_user.save()
            #return render(request, 'blog/includes/registration_done.html', {'new_user': new_user})
    #else:
     #   user_form = UserRegistrationForm()

    #return render(request, 'blog/includes/registration.html', {'user_form': user_form})

class RegisterView(FormView):
    form_class = UserRegistrationForm
    template_name = 'blog/includes/registration.html'

    def form_valid(self, form):

        if self.request.recaptcha_is_valid:
            form.save()
            return render(self.request, 'blog/includes/registration_done.html', self.get_context_data())
        return render(self.request, 'blog/includes/registration.html', self.get_context_data())



def posts_list(request):
    search_query = request.GET.get('search', '')
    if search_query:
        posts=Post.objects.filter(Q(title__icontains=search_query)|Q(body__icontains=search_query))
    else:
        posts=Post.objects.all()

    paginator = Paginator(posts, 3)


    page_number=request.GET.get('page', 1)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url= '?page={}'.format(page.previous_page_number())
    else:
        prev_url= ''
    if page.has_next():
        next_url= '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context= {
        'page_object': page,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
    }
    return render(request,'blog/index.html', context=context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class PostCreate(LoginRequiredMixin,View):
    raise_exception = True
    def get(self,request):
        form = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form':form})
    def post(self,request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request,'blog/post_create_form.html', context={'form':bound_form})


class PostUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model=Post
    model_form=PostForm
    template= 'blog/post_update_form.html'
    raise_exception = True

class PostDelete(LoginRequiredMixin,ObjectDeleteMixin,View):
    model = Post
    template = 'blog/post_delete_form.html'
    redirect_url = 'posts_list_url'
    raise_exception = True

class TagCreate(LoginRequiredMixin,View):

    raise_exception = True

    def get(self,request):
        form = TagForm()
        return render(request,'blog/tag_create.html',context={'form':form})
    def post(self,request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag= bound_form.save()
            return redirect(new_tag)
        return render(request,'blog/tag_create.html', context={'form':bound_form})
class TagUpdate(LoginRequiredMixin,ObjectUpdateMixin,View):
    model=Tag
    model_form=TagForm
    template= 'blog/tag_update_form.html'
    raise_exception = True


class TagDelete(LoginRequiredMixin,ObjectDeleteMixin,View):
    model = Tag
    template = 'blog/tag_delete_form.html'
    redirect_url = 'tags_list_url'
    raise_exception = True


def tags_list(request):
    tags =Tag.objects.all()
    return render(request,'blog/tags_list.html',context={'tags': tags})

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'

def index(request):
    return render (request,"blog/headlist.html")
