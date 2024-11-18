from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),  
    path("todo/",include("todo.urls")),
    # http://127.0.0.1:8000/api-auth/login/
    # http://127.0.0.1:8000/api-auth/logout/
    path('auth/', include('rest_framework.urls')),
]
