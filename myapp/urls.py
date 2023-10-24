from django.urls import path
from .views import ProfileView, ProfileFetchView


urlpatterns = [
    path('profile/', ProfileView.as_view(), name='profile-post'),
    path('profilefetcher',ProfileFetchView.as_view(),name='profile-fetch'),
]