from django.urls import path
from .views import *
            
   


urlpatterns = [
    path('', BasePage.as_view(), name='base'),
    path('home/', HomePage.as_view(), name='home'),
    path('about/', AboutPage.as_view(), name='about'),
    path('service/', ServicePage.as_view(), name='service'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', BlogCreatView.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post-edit'),
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post-delete'),



]



