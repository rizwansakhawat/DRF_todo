from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from .views import UserViewSet, CategoryViewSet, TaskviewSet, api_root

task_list = TaskviewSet.as_view({"get":"list", "post":"create"})
task_detail = TaskviewSet.as_view({
    "get":"retrieve" , "put":'update', "patch":"partial_update", "delete":"destroy"
})
task_highlight = TaskviewSet.as_view(
    {"get": "highlight"}, renderer_classes=[renderers.StaticHTMLRenderer])


user_list= UserViewSet.as_view( {"get":"list"})
user_detail = UserViewSet.as_view({"get":"retrieve"})
category_list= CategoryViewSet.as_view( {"get":"list"})
category_detail = CategoryViewSet.as_view({"get":"retrieve"})

urlpatterns = [
    path("", api_root, name="api_root"),
    path('tasks/', task_list, name="task_list"),
    path('tasks/<int:pk>/', task_detail, name="task_detail"),
    path('tasks/<int:pk>/highlight', task_highlight , name="task_highlight" ),
    path("users/", user_list, name="user_list"),
    path("users/<int:pk>/", user_detail, name='user_detail'),
    path("category/", category_list, name="category_list"),
    path("category/<int:pk>/", category_detail, name='category_detail'),
    
]

urlpatterns = format_suffix_patterns(urlpatterns) 





#============================ simple view urls
# from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
# from todo.views import TaskList, TaskDetail, UserList, UserDetail, api_root, CategoryList, CreateCategory

# urlpatterns = [
#     path("" ,  api_root, name="api_view"),
#     path("tasks/", TaskList.as_view(), name='task_list'),
#     path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
#     path('users/',UserList.as_view(), name="user_list"),
#     path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),
#     path('category/', CategoryList.as_view(), name="category_list" ),
#     path('create/category/', CreateCategory.as_view(), name="create_category")
# ]

# urlpatterns = format_suffix_patterns(urlpatterns) 
# #This allows your API to handle specific requests like .json or .api at the end of your endpoints.
