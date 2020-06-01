from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView


from .decorators import check_recaptcha

urlpatterns = [
    path('', index, name='headlist_url'),
    path('post/', posts_list, name='posts_list_url'),
    path('login/', LoginView.as_view(template_name='blog/includes/login.html'), name='login'),
    path('registration/',check_recaptcha(RegisterView.as_view()),name='register'),
    path('blog/logout',LogoutView.as_view(template_name='blog/index.html'),name='logout'),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name='post_detail_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('tags/', tags_list, name='tags_list_url'),
    path('tag/create/',TagCreate.as_view(),name='tag_create_url'),
    path('tag/<str:slug>/', TagDetail.as_view(), name='tag_detail_url'),
    path('tag/<str:slug>/update/', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/delete/', TagDelete.as_view(), name='tag_delete_url'),



]