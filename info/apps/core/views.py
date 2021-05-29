import requests
from .tasks import search_data_task
from django.shortcuts import render, redirect, reverse
from django.views.generic import View, TemplateView
from django.http import JsonResponse, HttpResponseRedirect
from bs4 import BeautifulSoup as bs
from .models import Post
import time
import math
from django.db.models import Max, Value
from django.db.models.functions import Coalesce


def render_result_page(request):
    try:
        all_entries = Post.objects.all()
        searched_item = Post.objects.filter().first()
        amount_of_products = Post.objects.all().count()

        data = {
            'all_entries': all_entries,
            'searched_item': searched_item,
            'amount_of_products': amount_of_products,
        }
        print(all_entries[0])
        return render(request, 'core/result.html', data)
    except:
        return render(request, 'core/result.html')


def render_loading_page(request):
    return render(request, "core/loading_page.html")


def render_base_page(request):
    if 'search' in request.POST:
        search_item = str(request.POST.get('search'))
        try:
            Post.objects.all().delete()
        except:
            pass
        if search_item == "":
            alert = "This product was not found. Please, try again if another name."
            print(alert)
            data = {
                'alert': alert,
            }
            return render(request, 'core/main.html', data)
        else:
            search_data_task.delay(search_item)
            return redirect('core:loading_page')
    return render(request, 'core/main.html')


class PostJasonListView(View):
    def get(self, *args, **kwargs):
        print(kwargs)
        upper = kwargs.get('num_posts')  # 100
        lower = upper - 16  # 0 if change the let visible variable on js and the handleGetData function, remember to also adjust here
        posts = list(Post.objects.values()[lower:upper])
        posts_size = len(Post.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'data': posts, 'max': max_size}, safe=False)

