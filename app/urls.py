from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

app_name='app'

urlpatterns=[
    path('',views.index,name='index'),
    path('(?P<album_id>[0-9]+)/',views.details,name='details'),
    path('add-album',views.add_album,name='add-album'),
    path('(?P<album_id>[0-9]+)/add-song',views.add_song,name='add-song'),
    path('(?P<album_id>[0-9]+)/delete-album',views.delete_album,name='delete-album'),
    path('signup',views.signup,name='signup'),
    #path('login',auth_views.LoginView.as_view(),name='login'),
    #path('logout',auth_views.LogoutView.as_view(),name='logout'),

    path('login',views.login_user,name='login'),
    path('logout',views.logout_user,name='logout'),
]