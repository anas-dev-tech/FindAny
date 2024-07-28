from django.urls import path, include


urlpatterns = [
    path('account/', include('allauth.urls')),
]





