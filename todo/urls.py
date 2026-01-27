from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from todo.views import TaskList, TaskDetail

urlpatterns = [
    path("tasks/", TaskList.as_view(), name='task' ),
    path("tasks/<int:pk>/", TaskDetail.as_view())
    # path("tasks/<int:pk>/", task_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns) 
#This allows your API to handle specific requests like .json or .api at the end of your endpoints.
