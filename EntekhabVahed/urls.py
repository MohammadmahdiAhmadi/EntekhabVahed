from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('mainApp/', include('mainApp.urls')),
    path('admin/', admin.site.urls),
]
