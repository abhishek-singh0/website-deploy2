from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('pub/', views.publication, name='pub'),
    path('caro/', views.caro, name='caro'),
    path('sect/', views.sect, name="sec"),
    path('test/', views.test, name="test"),
    path('research/', views.research, name="research"),
    path('team2/', views.team2, name="team2" ),
    path('gallery/', views.gallery, name="gallery"),
    path('404',views.error404, name='404'),

]