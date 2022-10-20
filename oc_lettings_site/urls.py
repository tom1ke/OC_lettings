from django.contrib import admin
from django.urls import path, include


def trigger_error(request):
    return 1 / 0


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('lettings.urls')),
    path('', include('profiles.urls')),
    path('sentry-debug/', trigger_error),
]
