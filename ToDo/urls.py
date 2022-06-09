
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    path('todos/', include('todos.urls')),
    path('admin/', admin.site.urls),
    path('', views.index)
]
urlpatterns += staticfiles_urlpatterns()
