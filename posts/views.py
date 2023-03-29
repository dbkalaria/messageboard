from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'all_post_list'


class Tooltestview(View):
    def get(self, request):
        a  = request.query_params.get("num_1", None)
        b = request.query_params.get("num_2", None)
        c = a/b
        return HttpResponse(c)