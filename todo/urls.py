from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo.views import TaskList, TaskDetail, UserList, UserDetail

urlpatterns = [
    path("tasks/", TaskList.as_view(), name='task' ),
    path("tasks/<int:pk>/", TaskDetail.as_view()),
    path('users/',UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns) 
#This allows your API to handle specific requests like .json or .api at the end of your endpoints.
