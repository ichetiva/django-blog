from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from .forms import CreatePostForm
from .models import Post


class ListPostsView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    context_object_name = "posts"


class DetailPostView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    context_object_name = "post"
    pk_url_kwarg = "post_id"


class CreatePostView(CreateView):
    model = Post
    template_name = "blog/post_create.html"
    form_class = CreatePostForm


class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy("list-posts")
    pk_url_kwarg = "post_id"
