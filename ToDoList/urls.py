
from django.contrib import admin
from django.urls import path
from todoapp.views import home, open_task, delete_task, close_task

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home, name='home'),
    path("open-task/<int:task_id>/", open_task, name="open_task"),
    path("delete-task/<int:task_id>/", delete_task, name="delete_task"),
    path("close-task/<int:task_id>/", close_task, name="close_task"),

]
