from django.contrib import admin
from django.urls import path
from . import views

app_name = 'apps.core'
urlpatterns = [
    path('', views.render_base_page, name='main'),
    path('result/', views.render_result_page, name='result'),
    path('loading_page/', views.render_loading_page, name='loading_page'),
    path('newresult/<int:num_posts>/', views.PostJasonListView.as_view(), name='posts-json-view')
]