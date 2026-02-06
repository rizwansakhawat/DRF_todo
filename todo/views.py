from .models import Task, Category
from .serializers import TaskSerializer, UserSerializer, CaterorySerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions, viewsets, renderers
from django.contrib.auth.models import User
from .permission import IsOwnerOrReadOnly, IsOwnerIsAdminOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.decorators import action


########### api root view
@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user_list", request=request, format=format),
            "tasks": reverse("task_list", request=request, format=format),
            "category": reverse("category_list", request=request, format=format),
            # "create_category":reverse("create_category", request=request, format=format)  
        })

##### viewsets& routers

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset =User.objects.all()
    serializer_class= UserSerializer
    
class TaskviewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CaterorySerializer



    
 
    
    
#==========================================
# ######## generics class base 

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class CategoryList(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CaterorySerializer
    
# class CreateCategory(generics.ListCreateAPIView):
#     queryset= Category.objects.all()
#     serializer_class = CaterorySerializer
#     permission_classes = [permissions.IsAdminUser]


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# #########  class base view with mixins
# from rest_framework import mixins
# from rest_framework import generics

# # list of all tasks
# class TaskList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    
#     queryset= Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly]

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)

    
# # task detail view    
# class TaskDetail(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerIsAdminOrReadOnly]

    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    
# ### end genirc class base view


#=============================================




######## class base views

# class TaskList(APIView):
#     """all tasks list """
#     def get(self, request, format=None):
#         tasks= Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class TaskDetail(APIView):
#     """
#     retrieve , update, or delete,
#     """

#     def get_object(self, pk):
#         try:
#             return Task.objects.get(pk=pk)
#         except Task.DoesNotExist:
#             raise Http404
        
#     def get(self, request,pk , format=None):
#         tasks= self.get_object(pk)
#         serializer = TaskSerializer(tasks)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         task= self.get_object(pk=pk)
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         task = self.get_object(pk)
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





#######  generic base views

# from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# class TaskList(ListCreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer


# class TaskDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer




# from django.shortcuts import render

# # Create your views here.
# from .models import Task
# from .serializers import TaskSerializer
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response


# @api_view(["GET","POST"])
# def task_list(request):
#     """
#     list of all TASK VIEW
#     """

#     if request.method == "GET":
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)
    
#     elif request.method == "POST":
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    
# @api_view(["GET", "PUT", "DELETE"])
# def task_detail(request, pk , format=None):
#     """
#     Docstring for task_detail
    
#     :param request: Description
#     :param pk: Description
#     """
#     try:
#         task = Task.objects.get(pk=pk)
        
#     except Task.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == "GET":
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)
    
#     elif request.method == "PUT":
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == "DELETE":
#         task.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)