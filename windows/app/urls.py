from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_windows/', views.all_windows, name='all_windows'),
    path('window/<int:window_id>/', views.window_detail, name='window'),
    path('all_glasses/', views.all_glasses, name='all_glasses')
]