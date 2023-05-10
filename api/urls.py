from django.urls import path
from api import views

urlpatterns = [
    path("tasks", views.TasksView.as_view(), name="tasks_view"),
    path("tasks/<id_arg>", views.TaskView.as_view(), name="task_view"),
    path("new", views.NewTaskView.as_view(), name="new_task_view")
]