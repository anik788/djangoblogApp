from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from blog.models import Post
from blog.forms import PostUpdateForm, PostForm


def home(request, *args, **kwargs):
    return HttpResponse("This is Home Page")


def post_list(request, *args, **kwargs):
    posts = Post.objects.filter(status='active').order_by('id')
    response = {
        "posts": posts
    }
    return render(request, 'blog/post_list.html', response)


def post_detail(request, post_id, *args, **kwargs):
    post = Post.objects.get(id=post_id)
    response = {
        "post": post
    }
    return render(request, 'blog/post_detail.html', response)


# def post_create(request, *args, **kwargs):
#     empty_form = None
#     if request.method == 'POST':
#         data = request.POST
#         form_data = PostCreateForm(data=data)
#         if form_data.is_valid():
#             cl_data = form_data.cleaned_data
#             title = cl_data.get('title')
#             body = cl_data.get('body', None)
#             status = cl_data.get('status', 'active')
#             post = Post.objects.create(title=title, body=body, status=status)
#             return redirect('blog:post_detail', post_id=post.id)
#     else:
#         empty_form = PostCreateForm()
#     return render(request, 'blog/post_create.html', {'empty_form': empty_form})


def post_create(request, *args, **kwargs):
    empty_form = None
    if request.method == 'POST':
        data = request.POST
        form_data = PostForm(data=data)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog:post_detail', post_id=form_data.instance.id)
        else:
            response = {
                'empty_form': empty_form,
                'error': form_data.errors if form_data.errors else None,
            }
            return render(request, 'blog/post_create.html', context=response)
    else:
        empty_form = PostForm()
    return render(request, 'blog/post_create.html', {'empty_form': empty_form})


# def post_update(request, post_id, *args, **kwargs):
#     empty_form = None
#     post_obj = Post.objects.get(id=post_id)
#     if request.method == 'POST':
#         data = request.POST
#         form_data = PostUpdateForm(data=data)
#         if form_data.is_valid():
#             cl_data = form_data.cleaned_data
#             if cl_data.get('title', None):
#                 post_obj.title = cl_data['title']
#                 post_obj.save()
#             if cl_data.get('body', None):
#                 post_obj.body = cl_data['body']
#                 post_obj.save()
#             if cl_data.get('status', None):
#                 post_obj.status = cl_data['status']
#                 post_obj.save()
#             return redirect('blog:post_detail', post_id=post_id)
#     else:
#         data = {
#             'title': post_obj.title,
#             'body': post_obj.body,
#             'status': post_obj.status
#         }
#         empty_form = PostUpdateForm(data=data)
#     return render(request, 'blog/post_create.html', {'empty_form': empty_form})


def post_update(request, post_id, *args, **kwargs):
    empty_form = None
    post_obj = Post.objects.get(id=post_id)
    if request.method == 'POST':
        data = request.POST
        form_data = PostUpdateForm(data=data, instance=post_obj)
        if form_data.is_valid():
            form_data.save()
            return redirect('blog:post_detail', post_id=post_id)
    else:
        empty_form = PostUpdateForm(instance=post_obj)
    return render(request, 'blog/post_create.html', {'empty_form': empty_form})


def post_delete(request, post_id, *args, **kwargs):
    Post.objects.get(id=post_id).delete()
    return redirect('blog:post_list')


# ---------------------------------class based View------------------

class PostListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateView, self).form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdateView, self).form_valid(form)

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post_obj = self.get_object()
        if self.request.user == post_obj.author:
            return True
        return False
