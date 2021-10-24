from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('games/', views.games_index, name='index'),
    path('games/<int:game_id>/', views.game_detail, name='detail'),
    path('games/create/', views.GameCreate.as_view(), name='game_create'),
    path('games/<int:pk>/update/', views.GameUpdate.as_view(), name='game_update'),
    path('games/<int:pk>/delete/', views.GameDelete.as_view(), name='game_delete'),
    path('games/<int:game_id>/add_play/', views.add_play, name='add_play'),
    path('games/<int:game_id>/add_photo/', views.add_photo, name='add_photo'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
