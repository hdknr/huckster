from django.urls import path, include

urlpatterns = [
    path('oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]
