from django.urls import path
from . import views
from first_app.views import (
    add_task,
    show_task,
    edit_task,
    delete_task,
    complete_task,
)

urlpatterns = [
    path("", views.home, name="Homepage"),
    path("add_task/", views.add_task, name="add_task"),
    path("show_task/", views.show_task, name="show_tasks"),
    path("edit_task/", views.edit_task, name="edit_task"),
    path("delete_task/", views.delete_task, name="delete_task"),
    path("complete_task/", views.complete_task, name="complete_task"),
    path("completed_tasks/", views.completed_tasks, name="completed_tasks"),
]
