from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api_app.views import RecipesInfoViewSet


defaultRouter = routers.DefaultRouter()

defaultRouter.register('recipes', RecipesInfoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(defaultRouter.urls)),
]