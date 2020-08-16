from django.contrib import admin
from django.urls import path, include

from django.views.i18n import JavaScriptCatalog


# 'recurrence' to the existing 'packages' tuple.
js_info_dict = {
    'packages': ('recurrence', ),
}

urlpatterns = [
    path("", include("apps.api.urls", namespace="api")),
    path(r'^jsi18n/$', JavaScriptCatalog.as_view(), js_info_dict),
    path("auth/", include('rest_framework_social_oauth2.urls')),
    path('jet/', include('jet.urls', namespace='jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    path('admin/', admin.site.urls),
]
