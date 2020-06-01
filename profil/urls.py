from django.urls import path
from .views import profile,ChangeUserInfoView,BBPasswordChangeView
from blog.views import RegisterDoneView


urlpatterns = [
    path('register/done/',RegisterDoneView.as_view(),name='register_done'),

    path('profile/', profile, name='profile'),
    path('change/', ChangeUserInfoView.as_view(),name='profile_change'),
    path('password/change/',BBPasswordChangeView.as_view(),name='password_change'),
    ]