from django.shortcuts import render, redirect, reverse

from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return redirect(reverse('login'))
        return super().get(request, *args, **kwargs)
