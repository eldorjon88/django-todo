from django.urls import path

from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.get_task_list_view, name='list'),
    path('add/', views.add_task_view, name='add'),
    path('detail/<str:task_id>', views.task_detail_view, name='detail'),
]
