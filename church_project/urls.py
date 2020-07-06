from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("", include("apps.accounts.urls", namespace="accounts")),
    path("auth/", include('rest_framework_social_oauth2.urls')),
    path('jet/', include('jet.urls', namespace='jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
]
