from django.urls import path ,include
from .api import ToDoAPIViewSet
from rest_framework import routers



router = routers.DefaultRouter()
router.register('todo', ToDoAPIViewSet)






app = 'todo'


urlpatterns = [
    path('', include(router.urls)),
]


