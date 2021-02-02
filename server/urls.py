from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from profiles.views import pull_request, issue, list_leaderboard
from django.contrib.auth import views as auth_views


schema_view = get_schema_view(
   openapi.Info(
      title="Leaderboard project for NITRR Hackfest",
      default_version='v1',
      description="Swagger API UI for Leaderboard project of NITRR Hackfest"
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('pull_request/', pull_request),
    path('issue/', issue),
    path('docs/', schema_view.with_ui('swagger',cache_timeout=0), name = 'schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    path('leaderboard/', list_leaderboard, name='view_leaderboard')
]
