from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth.forms import UserCreationForm


class SignUpView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "registration/sign_up.html", {"form": UserCreationForm()})

    def post(self, *args, **kwargs):
        form = UserCreationForm(self.request.POST)

        if form.is_valid():
            form.save()
            return redirect(reverse_lazy("list-posts"))
        else:
            return render(self.request, "registration/sign_up.html", {"form": UserCreationForm()})
