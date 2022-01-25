from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import HttpResponseForbidden

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


class CreatePostView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        return render(self.request, "blog/post_create.html", context={"form": CreatePostForm()})

    def post(self, *args, **kwargs):
        form = CreatePostForm(self.request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            db_post = Post(
                title=title,
                content=content,
                created_by=self.request.user
            )
            db_post.save()
            return redirect(reverse_lazy("post-detail", args=[db_post.id]))
        else:
            return render(self.request, "blog/post_create.html", context={"form": CreatePostForm()})


class DeletePostView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        db_post = Post.objects.get(id=kwargs["post_id"])
        if self.request.user.id != db_post.created_by.id:
            return HttpResponseForbidden("You haven't permissions for delete this post.")
        return render(self.request, "blog/post_confirm_delete.html", {"object": db_post.title})

    def post(self, *args, **kwargs):
        db_post = Post.objects.filter(id=kwargs["post_id"])
        db_post.delete()
        return redirect(reverse_lazy("list-posts"))
