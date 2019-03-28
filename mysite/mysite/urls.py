from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('craglists/', include('craglists.urls')),
    path('admin/', admin.site.urls),
]