
from django.shortcuts import render,get_object_or_404
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView , UpdateView, DeleteView
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
 



def home (request):
    context={
        'title':'Home',
        'posts':Post.objects.all(),
    }
    return render(request, 'blog/index.html',context)

def about (request):

    return render(request,'blog/about.html')

@login_required(login_url='login')
def post_detail(request, post_id):
    post=get_object_or_404(Post,pk=post_id)
    context={
        'title':'Detail',
        'post':post

    }

    return render(request, 'blog/detail.html',context)


class PostCreateView(CreateView):
    model = Post
    fields =['title' , 'content']
    template_name = 'blog/new_post.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form) 
    


class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model = Post
    fields =['title' , 'content']
    template_name = 'blog/post_update.html'

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)
    

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
        
class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model = Post
    success_url ='/'


    def test_func(self):
        post=self.get_object()
        if self.request.user == post.author:
            return True
       
        return False


def myblogs(request):
    
    context={
        'title':'Home',
        'posts':Post.objects.filter(author = request.user),
    }
    return render(request, 'blog/myblogs.html',context)


def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        post=Post.objects.filter(title__contains=search_query)
        
        return render(request, 'blog/search.html', {'search_query':search_query, 'post':post})
        
    else:
       
        return render(request, 'search.html',{})