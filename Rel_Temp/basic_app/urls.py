from django.urls import path
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('rel_temp/', views.rel_temp, name='rel_temp'),
]
