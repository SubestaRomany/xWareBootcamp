
from django.shortcuts import render,get_object_or_404
from . models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView , UpdateView, DeleteView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
 



def home (request):
    context={
        'title':'Home',
        'posts':Post.objects.all(),
    }
    return render(request, 'blog/index.html',context)

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

