from django.urls import path
from .views import *

# All urls here
urlpatterns = [
    #home url
    path('', TodoListCreateView.as_view() , name = 'home'),
    path('todo/<int:pk>', TodoDetailView.as_view(), name = 'todo_detail'),
    path('todo/<int:pk>/complete', TodoCompleteView.as_view(), name = 'todo_complete'),
    path('todo/<int:pk>/incomplete', TodoIncompleteView.as_view(), name = 'todo_incomplete'),

]
