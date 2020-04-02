from django.contrib import admin
from django.urls import path, include
from basic_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('relative/', include('basic_app.urls')),
    path('admin/', admin.site.urls),
]
