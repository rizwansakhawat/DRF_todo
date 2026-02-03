from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo.views import TaskList, TaskDetail, UserList, UserDetail, api_root

urlpatterns = [
    path("" ,  api_root, name="api_view"),
    path("tasks/", TaskList.as_view(), name='task_list'),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task_detail"),
    path('users/',UserList.as_view(), name="user_list"),
    path('users/<int:pk>/', UserDetail.as_view(), name="user_detail"),
    
]

urlpatterns = format_suffix_patterns(urlpatterns) 
#This allows your API to handle specific requests like .json or .api at the end of your endpoints.
