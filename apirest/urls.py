from django.urls import path, include
from rest_framework import routers
from apirest import views

router=routers.DefaultRouter()
router.register(r'developers', views.DeveloperViewSet)
router.register(r'projects', views.ProjectViewSet)

urlpatterns = [
    path('', include(router.urls))
]
