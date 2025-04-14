from django.urls import path, include

from rest_framework import routers

from planet import views


router = routers.SimpleRouter()
router.register(r'planet', views.PlanetView, basename='planet')

urlpatterns = router.urls