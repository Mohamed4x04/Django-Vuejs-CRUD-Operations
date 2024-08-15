from .serializers import ToDoSerializer
from .models import ToDo
from rest_framework import viewsets





class ToDoAPIViewSet(viewsets.ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer
    





    def get_queryset(self):
        queryset = ToDo.objects.filter(done=True)
        print(self.request.user)
        return queryset








    # def perform_create(self, serializer):
    #     return super().perform_create(serializer)
    
    
    # def perform_update(self, serializer):
    #     return super().perform_update(serializer)






    # def get_queryset(self):
    #     queryset = super(CLASS_NAME,self).get_queryset()
    #     queryset = queryset #TODO
    #     return queryset

























# def todo(request):
#     if request.method == 'GET':
#         pass
    
#     elif request.method == 'POST':
#         pass
    
#     elif request.method == 'PUT':
#         pass
    
#     elif request.method == 'DELETE':
#         pass
    
    
# class ToDoApp(ApiView):
#     def get():
#         pass
    
#     def post():
#         pass