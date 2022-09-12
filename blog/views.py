#from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category
from django.contrib.auth.mixins import LoginRequiredMixin
import math

class PostList(ListView):
    model=Post
    ordering='-pk'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context= super(PostList,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()

        page_numbers_range = 10 #최대 페이지 출력 수
        page = int(self.request.GET.get('page', '1'))
        pagelow=math.floor(page/10)*10+1
        page_list=list(i for i in range(pagelow,pagelow+10))
        context['page_list']=page_list
        return context

    



class PostDetail(DetailView):
    model=Post

    def get_context_data(self, **kwargs):
        context= super(PostDetail,self).get_context_data()
        context['categories']=Category.objects.all()
        context['no_category_post_count']=Post.objects.filter(category=None).count()
        return context

class PostCreate(LoginRequiredMixin, CreateView):
    model=Post
    fields=['title','content','head_image','upload_file','category']

    def form_valid(self, form):
        current_user=self.request.user
        if current_user.is_authenticated:
            form.instance.author=current_user
            return super(PostCreate, self).form_valid(form)
        else:
            return redirect('/blog/')

class PostModify(LoginRequiredMixin, UpdateView):
    model=Post
    fields=['title','content','head_image','upload_file','category']



def category_page(request,slug):
    if slug=='no_category':
        category='미분류'
        post_list=Post.objects.filter(category=None)
    else:
        category=Category.objects.get(slug=slug)
        post_list=Post.objects.filter(category=category)

    return render(
        request, 
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories':Category.objects.all(),
            'no_category_post_count':Post.objects.filter(category=None).count(),
            'category':category,
        }
    )

#def single_post_page(request,pk):
#    post=Post.objects.get(pk=pk)
#    return render(request,'blog/single_post_page.html',{'post':post})