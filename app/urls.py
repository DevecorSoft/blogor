from django.urls import path

from . import views

urlpatterns = {
    path('list/', views.blog_list, name='list'),
    path('blog-<blogId>/', views.blog, name='blogId'),
}
