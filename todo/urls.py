from django.urls import path ,include
from .api import ToDoAPIViewSet
from rest_framework import routers
from .views import todo_list


router = routers.DefaultRouter()
router.register('todo', ToDoAPIViewSet)






app = 'todo'


urlpatterns = [
    path('', todo_list,name='todo_list'),
    path('api/', include(router.urls)),

]


