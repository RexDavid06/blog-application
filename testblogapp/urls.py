from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('index/', views.index, name='index'),
    path('logout/', views.log_out, name='logout'),
    path('post_detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
    path('delete_post/<int:pk>/', views.delete_post, name='delete_post'),
    path('', views.AnonymousLoginView.as_view(), name='login'),

]