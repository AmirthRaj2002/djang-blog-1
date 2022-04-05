from django.urls import path
from . import views 
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:index>/', views.blog_post, name="post"),
]
