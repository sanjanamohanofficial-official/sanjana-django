from django.urls import path
from . import views

urlpatterns = [
    path('',                   views.home,          name='home'),
    path('add/',               views.add_player,    name='add_player'),
    path('players/',           views.view_players,  name='view_players'),
    path('edit/<int:pk>/',     views.edit_player,   name='edit_player'),
    path('delete/<int:pk>/',   views.delete_player, name='delete_player'),
    path('signup/',            views.signup_view,   name='signup'),
    path('login/',             views.login_view,    name='login'),
    path('logout/',            views.logout_view,   name='logout'),
]
