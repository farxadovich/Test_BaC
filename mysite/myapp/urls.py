from django.urls import path

from . import views


urlpatterns = [
    path('test/<int:category>/', views.test, name='test'),
    path('', views.index, name='index'),

]